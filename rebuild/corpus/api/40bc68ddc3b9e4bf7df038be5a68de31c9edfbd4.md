# GetListOfNodes Method (SettingNode)

GetListOfNodes Method (SettingNode)

Determines all settings nodes.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual void GetListOfNodes( 
   ref StringCollection colOfNodes,
   bool bAbsolutPath
)
```
```

```
```
public:
virtual void GetListOfNodes( 
   StringCollection^% colOfNodes,
   bool bAbsolutPath
)
```
```

#### Parameters

*colOfNodes*
:   Container to which existing settings nodes are output.

*bAbsolutPath*
:   Controls the output:

    True: Path of settings is absolute.

    False: Relative paths of settings are output.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | The value of the parameter object is NULL. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The object has not been initialized correctly. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The function failed. |

See Also

#### Reference

[SettingNode Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode.html)
  
[SettingNode Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode_members.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)