# SYMBLIB_FRAME(Int32) Property

SYMBLIB\_FRAME(Int32) Property

Plot frame to edit symbol # 15030. This property isn't indexed.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue SYMBLIB_FRAME( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ SYMBLIB_FRAME {
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

The plot frame which is used for editing the symbol.

If you assign a value using the Application Programming Interface, please ensure that the relevant master data are available in the project.

See Also

#### Reference

[SymbolLibraryPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList.html)
  
[SymbolLibraryPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_FRAME.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolLibraryPropertyList~SYMBLIB_FRAME(Int32))