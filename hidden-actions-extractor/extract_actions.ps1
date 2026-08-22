<#
.SYNOPSIS
  从 EPLAN Electric P8 安装目录的 DLL 中离线提取动作名(方法3,免运行 EPLAN)。

.DESCRIPTION
  原理:EPLAN 的动作是 .NET 类,动作名字符串(如 "gedRedraw"、"XEsGetProjectPropertyAction")
  以类名和注册属性字符串的形式存在于 Bin 目录的 DLL 元数据中。本脚本用 .NET 反射
  (ReflectionOnlyLoad,不执行任何 EPLAN 代码)枚举类型名和自定义属性,并辅以原始
  UTF-16 字符串扫描,输出候选动作名单。

  适用:EPLAN Electric P8 2.9(目录 2.9.x);2022/2024/2025/2026 版本同样适用。
  依赖:仅 Windows PowerShell 5.1(Windows 10/11 自带),无需安装任何东西。

.EXAMPLE
  # 自动查找 Bin 目录
  powershell -ExecutionPolicy Bypass -File extract_actions.ps1

  # 手动指定 Bin 目录
  powershell -ExecutionPolicy Bypass -File extract_actions.ps1 -BinPath "C:\Program Files\EPLAN\Electric P8\2.9.4\Bin"
#>
param(
    [string]$BinPath = "",          # EPLAN Bin 目录;留空则自动查找
    [string]$OutDir = ".\output"    # 输出目录
)

$ErrorActionPreference = "Continue"

# ---------------------------------------------------------------- 查找 Bin 目录
function Find-EplanBin {
    $roots = @(
        "C:\Program Files\EPLAN",
        "C:\Program Files (x86)\EPLAN",
        "D:\EPLAN", "E:\EPLAN", "F:\EPLAN"
    )
    foreach ($r in $roots) {
        if (-not (Test-Path $r)) { continue }
        # 目录结构两种可能: <root>\Electric P8\2.9.x\Bin 或 <root>\Platform\2.9.x\Bin
        foreach ($prod in @("Electric P8", "Platform")) {
            $prodDir = Join-Path $r $prod
            if (-not (Test-Path $prodDir)) { continue }
            $verDirs = Get-ChildItem $prodDir -Directory -ErrorAction SilentlyContinue |
                Where-Object { $_.Name -match "^2\.\d|^20\d\d" } |
                Sort-Object Name -Descending
            foreach ($vd in $verDirs) {
                $bin = Join-Path $vd.FullName "Bin"
                if (Test-Path (Join-Path $bin "Eplan.EplApi.AFu.dll")) { return $bin }
            }
        }
    }
    return $null
}

# ---------------------------------------------------------------- 工具函数
$script:Results = New-Object System.Collections.ArrayList
$script:Seen = @{}

function Add-Result($dll, $kind, $name, $extra) {
    $key = "$kind|$name"
    if ($script:Seen.ContainsKey($key)) { return }
    $script:Seen[$key] = $true
    [void]$script:Results.Add([ordered]@{ dll = $dll; kind = $kind; name = $name; extra = $extra })
}

function Test-ActionName($s) {
    # 动作名形态:纯 ASCII 字母数字下划线,长度 3~80
    if ($s -notmatch '^[A-Za-z][A-Za-z0-9_]{2,79}$') { return $false }
    # 过滤明显不是动作的公共词汇
    if ($s -match '^(System|Microsoft|Windows|Nullable|Func|Action|Object|String|Int|Void|Boolean|Exception|EventArgs|Attribute|EventArgs|Get|Set)$') { return $false }
    return $true
}

function Invoke-ScanDll($dllPath) {
    $dllName = Split-Path $dllPath -Leaf

    # ---- 通道1: .NET 反射(类名 + 注册属性)
    $asm = $null
    try { $asm = [Reflection.Assembly]::ReflectionOnlyLoadFrom($dllPath) } catch { }
    if ($asm) {
        $types = @()
        try { $types = $asm.GetTypes() }
        catch [Reflection.ReflectionTypeLoadException] {
            # 依赖缺失时部分类型仍可读
            $types = @($_.Exception.Types | Where-Object { $_ -ne $null })
        } catch { $types = @() }

        foreach ($t in $types) {
            try {
                $tn = $t.Name
                if (-not $tn) { continue }
                # 类名本身像动作名(后缀 Action 或 X 前缀家族)
                if ($tn -match 'Action$' -or $tn -match '^X[A-Z][A-Za-z0-9]+$') {
                    if (Test-ActionName $tn) { Add-Result $dllName "typename" $tn $t.FullName }
                }
                # 注册属性里的字符串参数(动作注册名)
                foreach ($cad in $t.GetCustomAttributesData()) {
                    $attrName = $cad.AttributeType.Name
                    if ($attrName -notmatch 'Declare|Register|Action') { continue }
                    foreach ($arg in $cad.ConstructorArguments) {
                        if ($arg.Value -is [string] -and $arg.Value.Length -gt 0) {
                            $v = $arg.Value
                            if (Test-ActionName $v) {
                                Add-Result $dllName "attribute" $v "$($t.FullName) [$attrName]"
                            }
                        }
                    }
                }
            } catch { }
        }
    }

    # ---- 通道2: 原始 UTF-16 字符串扫描(.NET 字符串以 UTF-16LE 存储)
    try {
        $bytes = [IO.File]::ReadAllBytes($dllPath)
        $text = [Text.Encoding]::Unicode.GetString($bytes)
        $rx = [regex]'[\x20-\x7E]{4,}'
        $hits = $rx.Matches($text)
        foreach ($h in $hits) {
            $s = $h.Value.Trim()
            if (Test-ActionName $s) {
                # 只保留动作样式的字符串:X 前缀家族 / Action 后缀 / 全小写动作词
                if ($s -match 'Action$' -or $s -match '^X[A-Z][A-Za-z0-9]+$' -or $s -cmatch '^[a-z][a-z0-9]+$') {
                    Add-Result $dllName "utf16string" $s ""
                }
            }
        }
    } catch { }
}

# ---------------------------------------------------------------- 主流程
if (-not $BinPath) {
    Write-Host "正在自动查找 EPLAN Bin 目录 ..." -ForegroundColor Cyan
    $BinPath = Find-EplanBin
    if (-not $BinPath) {
        Write-Host "未找到 Bin 目录。请用 -BinPath 参数手动指定,例如:" -ForegroundColor Red
        Write-Host '  powershell -ExecutionPolicy Bypass -File extract_actions.ps1 -BinPath "C:\Program Files\EPLAN\Electric P8\2.9.4\Bin"'
        exit 1
    }
}
if (-not (Test-Path $BinPath)) { Write-Host "Bin 目录不存在: $BinPath" -ForegroundColor Red; exit 1 }

Write-Host "Bin 目录: $BinPath" -ForegroundColor Cyan
$dlls = Get-ChildItem $BinPath -Filter *.dll | Sort-Object Name
Write-Host "找到 $($dlls.Count) 个 DLL,开始扫描 ..." -ForegroundColor Cyan

$i = 0
foreach ($dll in $dlls) {
    $i++
    if ($i % 20 -eq 0) { Write-Host "  进度 $i/$($dlls.Count) ..." }
    Invoke-ScanDll $dll.FullName
}

# ---------------------------------------------------------------- 输出
if (-not (Test-Path $OutDir)) { New-Item -ItemType Directory -Path $OutDir | Out-Null }

$json = $script:Results | ConvertTo-Json -Depth 4
$json | Out-File (Join-Path $OutDir "action_details.json") -Encoding UTF8

$candidates = $script:Results | ForEach-Object { $_.name } | Sort-Object -Unique
$candidates | Out-File (Join-Path $OutDir "action_candidates.txt") -Encoding UTF8

Write-Host ""
Write-Host "完成!" -ForegroundColor Green
Write-Host "  候选动作名: $($candidates.Count) 个 -> $(Join-Path $OutDir 'action_candidates.txt')"
Write-Host "  详细来源:            -> $(Join-Path $OutDir 'action_details.json')"
Write-Host ""
Write-Host "下一步: python probe_eplan_pages.py $(Join-Path $OutDir 'action_candidates.txt')" -ForegroundColor Cyan
