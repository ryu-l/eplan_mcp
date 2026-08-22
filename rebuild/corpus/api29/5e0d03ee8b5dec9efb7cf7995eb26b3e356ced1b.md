# ARTICLE_PLCISBUSCOUPLER(Int32) Property

ARTICLE\_PLCISBUSCOUPLER(Int32) Property

Bus coupler / head station # 22019. This property isn't indexed.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public MDPropertyValue ARTICLE_PLCISBUSCOUPLER( 
   int index
) {get; set;}
```
```

```
```
public:
property MDPropertyValue^ ARTICLE_PLCISBUSCOUPLER {
   MDPropertyValue^ get(int index);
   void set (int index, MDPropertyValue^ value);
}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type System.Boolean.

Remarks

Property of a part variant. Identifies a device as a bus coupler or as a head station. In the case of a head station the Rack property has to be filled additionally for the respective PLC card.

See Also

#### Reference

[MDPartsDatabaseItemPropertyList Class](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList.html)
  
[MDPartsDatabaseItemPropertyList Members](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList_members.html)
  
[Overload List](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_PLCISBUSCOUPLER.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_PLCISBUSCOUPLER(Int32))