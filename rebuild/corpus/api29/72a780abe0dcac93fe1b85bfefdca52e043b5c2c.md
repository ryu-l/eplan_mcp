# PropertyPlacements Property (SymbolReference)

PropertyPlacements Property (SymbolReference)

Returns [Eplan.EplApi.DataModel.Graphics.PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html)s assigned to the SymbolReference.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyPlacement[] PropertyPlacements {get;}
```
```

```
```
public:
property array<PropertyPlacement^>^ PropertyPlacements {
   array<PropertyPlacement^>^ get();
}
```
```

#### Property Value

[Eplan.EplApi.DataModel.Graphics.PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html)s assigned to the SymbolReference.

Remarks

When a new object was created by API, the displayed properties are set from original default schema of the symbol, even if another was set as default by user. Please use property SymbolReference.PropertyPlacementsSchemas.Selected to change displayed properties schema.

See Also

#### Reference

[SymbolReference Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)
  
[SymbolReference Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference_members.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~PropertyPlacements)