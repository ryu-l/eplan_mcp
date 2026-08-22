# ARTICLEREF_LENGTH_SUM Property

ARTICLEREF\_LENGTH\_SUM Property

Total length with unit of the project # 20513.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue ARTICLEREF_LENGTH_SUM {get; set;}
```
```

```
```
public:
property PropertyValue^ ARTICLEREF_LENGTH_SUM {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type .

Remarks

This property is read-only..

This property totals up the lengths of all the functions (for example connections, routing paths, busbars, etc.) having the same part. The length unit is specified in the project settings for connections. You can use the property in forms for the parts list, for example in calculation formulas for calculating the order length.

See Also

#### Reference

[MergedArticleReferencePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList.html)
  
[MergedArticleReferencePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLEREF_LENGTH_SUM.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLEREF_LENGTH_SUM())