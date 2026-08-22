# StartObject Property

StartObject Property

Returns the first of two [Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)s connected by this connection3D.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Function3D StartObject {get;}
```
```

```
```
public:
property Function3D^ StartObject {
   Function3D^ get();
}
```
```

#### Property Value

- the first of two [Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)s connected by this connection,
- `null` when there is no Function3D on this end of the connection.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when it is impossible to read the Function3D from project. |

Remarks

Name of 3d object can be different from value property of CONNECTION\_SOURCE or CONNECTION\_DESTINATION. If this connection is generated based on regular connection then those properties represents names of 2D source/target.

See Also

#### Reference

[Connection3D Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Connection3D.html)
  
[Connection3D Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Connection3D_members.html)
  
[Function3D Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Connection3D~StartObject)