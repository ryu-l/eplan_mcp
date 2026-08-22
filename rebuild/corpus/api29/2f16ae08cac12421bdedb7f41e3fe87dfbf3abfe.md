# PROJ_REVISION_LOG_TIME(Int32) Property

PROJ\_REVISION\_LOG\_TIME(Int32) Property

Revision time (change tracking) # 10159.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue PROJ_REVISION_LOG_TIME( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ PROJ_REVISION_LOG_TIME {
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

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Time when a project was changed during a revision. The time display can be specified in the project settings. A max. of 1,000 records allowed.

See Also

#### Reference

[ProjectPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList.html)
  
[ProjectPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_LOG_TIME.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISION_LOG_TIME(Int32))