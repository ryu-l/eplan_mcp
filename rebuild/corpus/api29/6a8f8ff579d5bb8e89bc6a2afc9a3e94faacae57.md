# FUNC_FORM_CONNECTIONDIAGRAM(Int32) Property

FUNC\_FORM\_CONNECTIONDIAGRAM(Int32) Property

Form for wiring diagram # 20234. This property isn't indexed.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_FORM_CONNECTIONDIAGRAM( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_FORM_CONNECTIONDIAGRAM {
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

Allows for a separate form for wiring diagrams to be stated at the main function of a device. Wiring diagrams consist of several connection diagrams and are used to output information about connected conductors and targets. (Additional information can be obtained in the help system in the section "Generating wiring diagrams".)

If you assign a value via the API interface, please make sure that the corresponding master data is available in the project.

See Also

#### Reference

[FunctionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList.html)
  
[FunctionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_FORM_CONNECTIONDIAGRAM.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_FORM_CONNECTIONDIAGRAM(Int32))