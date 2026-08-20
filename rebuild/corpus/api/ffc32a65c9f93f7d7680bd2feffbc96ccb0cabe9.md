# LocalTemplates Property

LocalTemplates Property

Returns set of local templates assigned to this object or to its segment template.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public StorableObject[] LocalTemplates {get;}
```
```

```
```
public:
property array<StorableObject^>^ LocalTemplates {
   array<StorableObject^>^ get();
}
```
```

Remarks

If [SegmentTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~SegmentTemplate.html) is assigned then set of local templates from segment template are returned. If `not` then set of local templates from this object is returned.

See Also

#### Reference

[PlanningSegment Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)
  
[PlanningSegment Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment_members.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)