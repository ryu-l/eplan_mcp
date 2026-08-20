# Close Method (Project)

Close Method (Project)

Closes the project. Must not be called before Remove()

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void Close()
```
```

```
```
public:
void Close();
```
```

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the project was already closed. |

Remarks

Warning: exception [ObjectNotCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectNotCreatedException.html) is thrown when getting/setting properties or calling methods (except [ProjectManager.OpenProject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~OpenProject(String).html)) on closed project.

See Also

#### Reference

[Project Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html)
  
[Project Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project_members.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)