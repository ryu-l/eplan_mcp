# Open(String,Mode) Method

Open(String,Mode) Method

Opens an existing symbol library.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public static MDSymbolLibrary Open( 
   string strSymbolLibraryPath,
   MDSymbolLibrary.Mode eMode
)
```
```

```
```
public:
static MDSymbolLibrary^ Open( 
   String^ strSymbolLibraryPath,
   MDSymbolLibrary.Mode eMode
)
```
```

#### Parameters

*strSymbolLibraryPath*
:   filename of the library that will be opened

*eMode*
:   mode of Open method

#### Return Value

symbol library that is opened

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when readonly database is opened in exclusive mode. |

See Also

#### Reference

[MDSymbolLibrary Class](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibrary.html)
  
[MDSymbolLibrary Members](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibrary_members.html)
  
[Overload List](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibrary~Open.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibrary~Open(String,Mode))