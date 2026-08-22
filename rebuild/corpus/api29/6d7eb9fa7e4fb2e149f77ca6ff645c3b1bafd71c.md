# ClearSearchDB(Project) Method

ClearSearchDB(Project) Method

Clears the list of search results.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void ClearSearchDB( 
   Project pProject
)
```
```

```
```
public:
void ClearSearchDB( 
   Project^ pProject
)
```
```

#### Parameters

*pProject*
:   Project of which the list of search results will be cleared.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the project is not valid. |
| **ApplicationException** | \Internal interface for search could not be created. |
| **BaseException** | The method finished with errors. |

See Also

#### Reference

[Search Class](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search.html)
  
[Search Members](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search_members.html)
  
[Overload List](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~ClearSearchDB.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~ClearSearchDB(Project))