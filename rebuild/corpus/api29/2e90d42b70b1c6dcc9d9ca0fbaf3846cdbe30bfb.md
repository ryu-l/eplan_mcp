# Location Property (ContactImage)

Location Property (ContactImage)

Get or set the placement's location.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public override PointD Location {get; set;}
```
```

```
```
public:
property PointD Location {
   PointD get() override;
   void set (    PointD value) override;
}
```
```

Exceptions

| Exception | Description |
| --- | --- |
| [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) | Thrown when property or function can not be used for specific class. For example it is thrown when this property is called on [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) objects. |

Remarks

Setting value for Location change value of `AutoAlign` to `true`.

See Also

#### Reference

[ContactImage Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ContactImage.html)
  
[ContactImage Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ContactImage_members.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ContactImage~Location)