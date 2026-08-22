# SetDoubleSetting Method (ISettings)

SetDoubleSetting Method (ISettings)

Sets the value of settings on a given path.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
void SetDoubleSetting( 
   string strSettingPath,
   double dValue,
   int nIdx
)
```
```

```
```
void SetDoubleSetting( 
   String^ strSettingPath,
   double dValue,
   int nIdx
)
```
```

#### Parameters

*strSettingPath*
:   path to settings

*dValue*
:   value to set.

*nIdx*
:   0-based index of the setting

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingsPath` is `null`. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the value cannot be set. |

Remarks

Warning: double values are stored with precision to 15 digits only!

See Also

#### Reference

[ISettings Interface](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings.html)
  
[ISettings Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings_members.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings~SetDoubleSetting)