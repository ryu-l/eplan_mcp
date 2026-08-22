# FUNC_CROSSREFERENCEMAINFUNCTION(Int32) Property

FUNC\_CROSSREFERENCEMAINFUNCTION(Int32) Property

Cross-reference display: Auxiliary function as main function # 20314. This property isn't indexed.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_CROSSREFERENCEMAINFUNCTION( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_CROSSREFERENCEMAINFUNCTION {
   PropertyValue^ get(int index);
   void set (int index, PropertyValue^ value);
}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is activated at an auxiliary function, it will behave, in terms of the cross-reference display, like a main function, and the main function of the same device will automatically behave like an auxiliary function. If a contact image is displayed at the main function, it is not carried over to the auxiliary function, but remains at the main function.

If the property is activated for several functions of a device, a possible main function "wins", otherwise the graphically first function.

See Also

#### Reference

[FunctionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList.html)
  
[FunctionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_CROSSREFERENCEMAINFUNCTION.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_CROSSREFERENCEMAINFUNCTION(Int32))