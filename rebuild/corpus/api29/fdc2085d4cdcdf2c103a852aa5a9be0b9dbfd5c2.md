# PAGE_CREATIONTIME(Int32) Property

PAGE\_CREATIONTIME(Int32) Property

Creation time # 11002. This property isn't indexed, and is read-only.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue PAGE_CREATIONTIME( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ PAGE_CREATIONTIME {
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

The time the page was created. How the time is displayed can be configured in the project settings.

See Also

#### Reference

[PagePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList.html)
  
[PagePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_CREATIONTIME.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_CREATIONTIME(Int32))