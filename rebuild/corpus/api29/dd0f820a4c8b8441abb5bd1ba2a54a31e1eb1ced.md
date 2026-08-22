# PATHTEXT_FUNCTIONS(Int32) Property

PATHTEXT\_FUNCTIONS(Int32) Property

Affected functions # 19800. This property isn't indexed, and is read-only.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue PATHTEXT_FUNCTIONS( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ PATHTEXT_FUNCTIONS {
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

Lists all the functions for a path function text that adopt this function text from the path.

See Also

#### Reference

[PathTextPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PathTextPropertyList.html)
  
[PathTextPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PathTextPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PathTextPropertyList~PATHTEXT_FUNCTIONS.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PathTextPropertyList~PATHTEXT_FUNCTIONS(Int32))