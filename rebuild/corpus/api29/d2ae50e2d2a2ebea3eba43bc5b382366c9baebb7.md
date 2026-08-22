# FUNC_MAINCROSSREFERENCE(Int32) Property

FUNC\_MAINCROSSREFERENCE(Int32) Property

Cross-reference (only main functions) # 20306. This property isn't indexed, and is read-only.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_MAINCROSSREFERENCE( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_MAINCROSSREFERENCE {
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

Shows cross-references for possible main functions of the device. The function category has to match here. This property can be used to show a cross-reference on a black box to the same black box placed elsewhere.

See Also

#### Reference

[FunctionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList.html)
  
[FunctionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_MAINCROSSREFERENCE.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_MAINCROSSREFERENCE(Int32))