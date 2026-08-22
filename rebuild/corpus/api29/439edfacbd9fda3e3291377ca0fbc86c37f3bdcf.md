# DESIGNATION_FUNCTIONALASSIGNMENT(Int32) Property

DESIGNATION\_FUNCTIONALASSIGNMENT(Int32) Property

Functional assignment (main identifier) # 1300. This property isn't indexed, and is read-only.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue DESIGNATION_FUNCTIONALASSIGNMENT( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ DESIGNATION_FUNCTIONALASSIGNMENT {
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

This property is used as part of a name. In order to set it, member `NameParts` must be used on object which name will be changed. Additionally for setting this property on a Page object, a function Page::SetName() or the Page constructor can be used.

See Also

#### Reference

[ArticleReferencePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList.html)
  
[ArticleReferencePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~DESIGNATION_FUNCTIONALASSIGNMENT.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~DESIGNATION_FUNCTIONALASSIGNMENT(Int32))