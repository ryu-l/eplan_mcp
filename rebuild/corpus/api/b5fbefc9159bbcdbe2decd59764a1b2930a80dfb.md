# CreateTransient Method (PlaceHolder)

CreateTransient Method (PlaceHolder)

Creates transient and not placed PlaceHolder object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public override void CreateTransient( 
   Project oProject
)
```
```

```
```
public:
void CreateTransient( 
   Project^ oProject
) override
```
```

#### Parameters

*oProject*
:   [Eplan.EplApi.DataModel.Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) the PlaceHolder will be assign to.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the PlaceHolder cannot be created. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the PlaceHolder has already been created. |

Remarks

After creation object is not stored in project database. It can be inserted into database after execution of [Eplan.EplApi.DataModel.Placement.CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~CopyTo(Group).html).

See Also

#### Reference

[PlaceHolder Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder.html)
  
[PlaceHolder Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder_members.html)
  
[Project Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)