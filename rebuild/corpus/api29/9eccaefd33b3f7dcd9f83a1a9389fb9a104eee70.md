# SYMBLIB_NAME(Int32) Property

SYMBLIB\_NAME(Int32) Property

Symbol library # 15000. This property isn't indexed, and is read-only.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue SYMBLIB_NAME( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ SYMBLIB_NAME {
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

Name of the symbol library, determined from the database name.

See Also

#### Reference

[SymbolLibraryPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList.html)
  
[SymbolLibraryPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_NAME.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_NAME(Int32))