# ARTICLE_CABLEDISPLAYFORM(Int32) Property

ARTICLE\_CABLEDISPLAYFORM(Int32) Property

Cable assignment diagram form # 22034. This property isn't indexed.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue ARTICLE_CABLEDISPLAYFORM( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ ARTICLE_CABLEDISPLAYFORM {
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

Property of a part variant. Shows the form to be used for the cable assignment diagram. When selecting a part the contents of this property are transferred to the main function. For the report, only those cables are considered which are assigned a form in the property "Cable assignment diagram form". All other cables are ignored.

See Also

#### Reference

[ArticlePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList.html)
  
[ArticlePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLEDISPLAYFORM.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLEDISPLAYFORM(Int32))