# DMG_VIEWPLACEMENT_BUILDINGAREA_DESCRIPTION(Int32) Property

DMG\_VIEWPLACEMENT\_BUILDINGAREA\_DESCRIPTION(Int32) Property

Model view: Layout space description # 36505. This property isn't indexed, and is read-only.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue DMG_VIEWPLACEMENT_BUILDINGAREA_DESCRIPTION( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ DMG_VIEWPLACEMENT_BUILDINGAREA_DESCRIPTION {
   PropertyValue^ get(int index);
   void set (int index, PropertyValue^ value);
}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This property is read-only..

Description of the layout space for which the model view, drilling view or copper unfold was created.

See Also

#### Reference

[ViewPlacementPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList.html)
  
[ViewPlacementPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList_members.html)
  
[Overload List](topic1679.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_BUILDINGAREA_DESCRIPTION(Int32))