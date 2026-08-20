# DMPLAOBJECT_DIGITAL_PLCINPUT_COUNT Property

DMPLAOBJECT\_DIGITAL\_PLCINPUT\_COUNT Property

Total number of digital PLC inputs # 44028.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue DMPLAOBJECT_DIGITAL_PLCINPUT_COUNT {get; set;}
```
```

```
```
public:
property PropertyValue^ DMPLAOBJECT_DIGITAL_PLCINPUT_COUNT {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only..

Shows the sum of the digital PLC inputs for the current planning object and the subordinate planning objects and (in accordance with the tree structure in the pre-planning navigator). Digital PLC addresses are such addresses that have the data type "BOOL". This is not case-sensitive. Inputs and outputs are recognized by the direction of the PLC address.

See Also

#### Reference

[PlanningSegmentPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList.html)
  
[PlanningSegmentPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList_members.html)
  
[Overload List](topic2202.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)