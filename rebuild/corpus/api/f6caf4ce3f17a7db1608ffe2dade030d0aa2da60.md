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
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during connection generation. Please refer to the exception message. |

See Also

#### Reference

[Generate Class](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Generate.html)
  
[Generate Members](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Generate_members.html)
  
[Overload List](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Generate~Connections.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)