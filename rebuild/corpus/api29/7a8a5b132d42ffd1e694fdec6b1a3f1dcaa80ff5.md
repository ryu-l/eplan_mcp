# FUNC_ARTICLE_ASSEMBLY Property

FUNC\_ARTICLE\_ASSEMBLY Property

Assembly # 20905.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_ASSEMBLY {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_ARTICLE_ASSEMBLY {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

A collection of parts that belong to a device (e.g. a pushbutton with a normally open contact, the appropriate mounting and the button). An assembly has its own part number and can also contain (sub) assemblies.

Changes done on this property are also visible on properties: \* ARTICLEREF\_ASSEMBLY of corresponding [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html).

See Also

#### Reference

[PlanningSegmentPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList.html)
  
[PlanningSegmentPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~FUNC_ARTICLE_ASSEMBLY.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~FUNC_ARTICLE_ASSEMBLY())