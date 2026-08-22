# Move Method (Group)

Move Method (Group)

Move all [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s in a group by a [Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html) given as param.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void Move( 
   PointD pntMovement
)
```
```

```
```
public:
void Move( 
   PointD pntMovement
)
```
```

#### Parameters

*pntMovement*

Remarks

This method doesn't make sense for class "SymbolVariant". It always throws [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) for class "SymbolVariant".

See Also

#### Reference

[Group Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)
  
[Group Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group_members.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~Move)