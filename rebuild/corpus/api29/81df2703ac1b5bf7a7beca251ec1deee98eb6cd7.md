# PROJ_HIERARCHY_DOCUMENTSTRUCTURE(Int32) Property

PROJ\_HIERARCHY\_DOCUMENTSTRUCTURE(Int32) Property

Project structure: Document type # 10006. This property isn't indexed.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue PROJ_HIERARCHY_DOCUMENTSTRUCTURE( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ PROJ_HIERARCHY_DOCUMENTSTRUCTURE {
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

The document type valid only for pages and external documents is stored in this project structure. The KKS identifier is normally entered here.

See Also

#### Reference

[ProjectPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList.html)
  
[ProjectPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_DOCUMENTSTRUCTURE.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_HIERARCHY_DOCUMENTSTRUCTURE(Int32))