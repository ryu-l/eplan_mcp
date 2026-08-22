# ARTICLE_QUANTITY_IN_PROJECT_UNIT(Int32) Property

ARTICLE\_QUANTITY\_IN\_PROJECT\_UNIT(Int32) Property

Quantity / subset in unit of project # 20507. This property isn't indexed, and is read-only.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue ARTICLE_QUANTITY_IN_PROJECT_UNIT( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ ARTICLE_QUANTITY_IN_PROJECT_UNIT {
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

This property is read-only..

Quantity or subset of a part converted into the unit which is specified in the project settings. The units are not displayed. If the property "Subset / length" has a value (not 0), then this value is entered for "Quantity / subset" in reports, otherwise "Quantity" is used.

See Also

#### Reference

[ArticleReferencePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList.html)
  
[ArticleReferencePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLE_QUANTITY_IN_PROJECT_UNIT.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLE_QUANTITY_IN_PROJECT_UNIT(Int32))