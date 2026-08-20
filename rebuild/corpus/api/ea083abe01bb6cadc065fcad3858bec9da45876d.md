# ApplyRecord(String,Boolean) Method

ApplyRecord(String,Boolean) Method

Applies a record of values on a PlaceHolder object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual void ApplyRecord( 
   string strRecordName,
   bool bApplyPageAndProjectData
)
```
```

```
```
public:
virtual void ApplyRecord( 
   String^ strRecordName,
   bool bApplyPageAndProjectData
)
```
```

#### Parameters

*strRecordName*
:   Name of the record to apply.

*bApplyPageAndProjectData*
:   Whether the page and project data should be set.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown in case of missing parameters. |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |
| [System.ApplicationException](#) | The internal interface for place holders could not be created. |

See Also

#### Reference

[PlaceHolder Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder.html)
  
[PlaceHolder Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~ApplyRecord.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)