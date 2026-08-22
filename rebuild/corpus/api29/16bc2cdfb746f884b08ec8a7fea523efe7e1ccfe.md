# INTERRUPTIONPOINT_DESTINATION(Int32) Property

INTERRUPTIONPOINT\_DESTINATION(Int32) Property

Target of interruption point # 24000. This property isn't indexed, and is read-only.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue INTERRUPTIONPOINT_DESTINATION( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ INTERRUPTIONPOINT_DESTINATION {
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

Provides the (first) target of an interruption point for display in the cross-reference; only used internally.

See Also

#### Reference

[InterruptionPointPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointPropertyList.html)
  
[InterruptionPointPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointPropertyList~INTERRUPTIONPOINT_DESTINATION.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointPropertyList~INTERRUPTIONPOINT_DESTINATION(Int32))