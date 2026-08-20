# SYMB_CONNECTIONNUMBER(Int32) Property

SYMB\_CONNECTIONNUMBER(Int32) Property

Connection point number # 16001.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public MDPropertyValue SYMB_CONNECTIONNUMBER( 
   int index
) {get; set;}
```
```

```
```
public:
property MDPropertyValue^ SYMB_CONNECTIONNUMBER {
   MDPropertyValue^ get(int index);
   void set (int index, MDPropertyValue^ value);
}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 100.

Internal connection point number. Either a consecutive number or a "n" (for a variable connection number) or a "z" (for the last connection point with a variable connection number).

See Also

#### Reference

[MDSymbolPropertyList Class](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPropertyList.html)
  
[MDSymbolPropertyList Members](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPropertyList_members.html)
  
[Overload List](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPropertyList~SYMB_CONNECTIONNUMBER.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)