# GetSegmentDefinition Method

GetSegmentDefinition Method

Returns [Eplan.EplApi.DataModel.Planning.SegmentDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition.html) from this Project with given name.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public SegmentDefinition GetSegmentDefinition( 
   string strIdentName
)
```
```

```
```
public:
SegmentDefinition^ GetSegmentDefinition( 
   String^ strIdentName
)
```
```

#### Parameters

*strIdentName*
:   Identifying name of the segment definition to be found.

#### Return Value

Segment definition with given identifying name or `null` if such definition is not found.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when name is empty. |
| [System.ArgumentNullException](#) | Thrown when name is `null`. |

See Also

#### Reference

[Project Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html)
  
[Project Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project_members.html)
  
[SegmentDefinition Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)