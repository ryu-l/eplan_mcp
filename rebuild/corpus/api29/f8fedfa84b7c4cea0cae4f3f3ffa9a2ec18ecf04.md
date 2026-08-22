# FUNCTION3D_DESIGNATIONPREFIX_AUTOMATIC(Int32) Property

FUNCTION3D\_DESIGNATIONPREFIX\_AUTOMATIC(Int32) Property

Grouping sign for item designation (automatic) # 36002. This property isn't indexed, and is read-only.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNCTION3D_DESIGNATIONPREFIX_AUTOMATIC( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNCTION3D_DESIGNATIONPREFIX_AUTOMATIC {
   PropertyValue^ get(int index);
   void set (int index, PropertyValue^ value);
}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Shows the contents of the "Grouping sign for item designation" property (ID 36012). If no preceding sign is entered for the item, this is defined from the first superior item for which a preceding sign is entered in the "Grouping sign for item designation" property.

See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_DESIGNATIONPREFIX_AUTOMATIC.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_DESIGNATIONPREFIX_AUTOMATIC(Int32))