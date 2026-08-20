# PrepareMacros(Project,Boolean,Boolean,Boolean) Method

PrepareMacros(Project,Boolean,Boolean,Boolean) Method

Prepares and groups all elements belonging to a macro box or page macro.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool PrepareMacros( 
   Project oProject,
   bool bGroupMacroBoxes,
   bool bGroupPageMacros,
   bool bSetHandleOnMacroBoxes
)
```
```

```
```
public:
bool PrepareMacros( 
   Project^ oProject,
   bool bGroupMacroBoxes,
   bool bGroupPageMacros,
   bool bSetHandleOnMacroBoxes
)
```
```

#### Parameters

*oProject*
:   Project for which preparation should be performed. It has to be a macro project.

*bGroupMacroBoxes*
:   Group macro boxes with their contents.

*bGroupPageMacros*
:   Group contents of a page macro.

*bSetHandleOnMacroBoxes*
:   Activates handle for macro box. By this unwanted shifting of macro is prevented.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Project was set to a null reference. |
| [System.ArgumentException](#) | Project is invalid. |
| [System.ApplicationException](#) | Internal interface for master data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Macros cannot be prepared. |

See Also

#### Reference

[Masterdata Class](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Masterdata.html)
  
[Masterdata Members](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Masterdata_members.html)
  
[Overload List](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Masterdata~PrepareMacros.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)