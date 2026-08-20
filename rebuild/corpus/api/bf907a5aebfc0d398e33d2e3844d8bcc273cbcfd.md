# SetFilteredPropertyList(PlanningSegmentPropertyList) Method

SetFilteredPropertyList(PlanningSegmentPropertyList) Method

Sets the [Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList.html) that [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)s matching the filter must have.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void SetFilteredPropertyList( 
   PlanningSegmentPropertyList searchedPropList
)
```
```

```
```
public:
void SetFilteredPropertyList( 
   PlanningSegmentPropertyList^ searchedPropList
)
```
```

#### Parameters

*searchedPropList*
:   List of the P8 properties the [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)s matching the the filter. Cannot be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |

See Also

#### Reference

[PlanningSegmentsFilter Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlanningSegmentsFilter.html)
  
[PlanningSegmentsFilter Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlanningSegmentsFilter_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlanningSegmentsFilter~SetFilteredPropertyList.html)
  
[PlanningSegmentPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)