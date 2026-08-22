# DMPLAOBJECT_POWER_REQUIREMENT_TOTAL Property

DMPLAOBJECT\_POWER\_REQUIREMENT\_TOTAL Property

Total power consumption # 44011.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue DMPLAOBJECT_POWER_REQUIREMENT_TOTAL {get; set;}
```
```

```
```
public:
property PropertyValue^ DMPLAOBJECT_POWER_REQUIREMENT_TOTAL {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type .

Remarks

This property is read-only..

Displays the total of the required power consumption that was estimated for the realization of the current segment. To this purpose the required power consumption of the current segment (at a planning object) and of all the planning objects lying below this segment are added up. The property is available in reports.

See Also

#### Reference

[PlanningSegmentPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList.html)
  
[PlanningSegmentPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList_members.html)
  
[Overload List](topic2261.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DMPLAOBJECT_POWER_REQUIREMENT_TOTAL())