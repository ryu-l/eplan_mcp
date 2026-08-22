# GetPlugStrips Method

GetPlugStrips Method

Returns [Eplan.EplApi.DataModel.EObjects.PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html)s matching given filter.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PlugStrip[] GetPlugStrips( 
   FunctionsFilter filter
)
```
```

```
```
public:
array<PlugStrip^>^ GetPlugStrips( 
   FunctionsFilter^ filter
)
```
```

#### Parameters

*filter*
:   a [FunctionsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter.html), can be `null`

#### Return Value

\* [Eplan.EplApi.DataModel.EObjects.PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html)s matching given [FunctionsFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter.html). \* all [Eplan.EplApi.DataModel.EObjects.PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html)s when filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal used query throw exception. |

See Also

#### Reference

[DMObjectsFinder Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder.html)
  
[DMObjectsFinder Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder_members.html)
  
[PlugStrip Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html)
  
[FunctionsFilter Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlugStrips)