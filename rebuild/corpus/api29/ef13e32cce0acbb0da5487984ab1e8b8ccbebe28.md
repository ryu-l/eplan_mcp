# Connections(Page[],Boolean) Method

Connections(Page[],Boolean) Method

Updates connections on given pages from one project. Project is taken from first page.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void Connections( 
   Page[] arrayPages,
   bool bRebuildAllConnections
)
```
```

```
```
public:
void Connections( 
   array<Page^>^ arrayPages,
   bool bRebuildAllConnections
)
```
```

#### Parameters

*arrayPages*
:   Pages with connections to update.

*bRebuildAllConnections*
:   If true rebuilds all connections else updates only.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid project. |
| **ApplicationException** | The internal interface for generating connections could not be created. |
| **BaseException** | An error occurred during connection generation. Please refer to the exception message. |

See Also

#### Reference

[Generate Class](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Generate.html)
  
[Generate Members](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Generate_members.html)
  
[Overload List](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Generate~Connections.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Generate~Connections(Page[],Boolean))