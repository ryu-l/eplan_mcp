# FUNCTION3D_POWERDISSIPATION_SIMULTANEITYFACTOR(Int32) Property

FUNCTION3D\_POWERDISSIPATION\_SIMULTANEITYFACTOR(Int32) Property

Thermal design: Simultaneity factor (device) # 36045. This property isn't indexed.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNCTION3D_POWERDISSIPATION_SIMULTANEITYFACTOR( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNCTION3D_POWERDISSIPATION_SIMULTANEITYFACTOR {
   PropertyValue^ get(int index);
   void set (int index, PropertyValue^ value);
}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type System.Double.

Remarks

Deviating simultaneity factor for this device compared to the project properties. Is required for calculating the power dissipation.

See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](topic1516.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_POWERDISSIPATION_SIMULTANEITYFACTOR(Int32))