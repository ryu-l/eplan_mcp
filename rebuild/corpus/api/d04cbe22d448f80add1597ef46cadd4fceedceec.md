# SYMB_PREVENTPLACEMENT Property

SYMB\_PREVENTPLACEMENT Property

Prevent new placement # 16012.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue SYMB_PREVENTPLACEMENT {get; set;}
```
```

```
```
public:
property PropertyValue^ SYMB_PREVENTPLACEMENT {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.Boolean.

Remarks

Prevents the symbol being used in new schematics. If this property is activated, then the symbol is no longer shown in the project symbol selection, i.e. it can no longer be newly inserted. The symbol can still be edited in the master data.

See Also

#### Reference

[SymbolPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList.html)
  
[SymbolPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList~SYMB_PREVENTPLACEMENT.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)