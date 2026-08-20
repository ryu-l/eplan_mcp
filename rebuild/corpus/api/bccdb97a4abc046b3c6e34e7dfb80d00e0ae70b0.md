# SYMBLIB_SUPPLEMENTARYFIELD(Int32) Property

SYMBLIB\_SUPPLEMENTARYFIELD(Int32) Property

Supplementary field # 15901.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public MDPropertyValue SYMBLIB_SUPPLEMENTARYFIELD( 
   int index
) {get; set;}
```
```

```
```
public:
property MDPropertyValue^ SYMBLIB_SUPPLEMENTARYFIELD {
   MDPropertyValue^ get(int index);
   void set (int index, MDPropertyValue^ value);
}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Max. 1,000 supplementary fields for the symbol library that can be specified using the index.

See Also

#### Reference

[MDSymbolLibraryPropertyList Class](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibraryPropertyList.html)
  
[MDSymbolLibraryPropertyList Members](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibraryPropertyList_members.html)
  
[Overload List](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibraryPropertyList~SYMBLIB_SUPPLEMENTARYFIELD.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)