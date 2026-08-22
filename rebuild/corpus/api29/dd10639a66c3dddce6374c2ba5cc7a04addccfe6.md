# GetPart(String) Method

GetPart(String) Method

Gets the part with the given part number. If there are several variants of that part, the first one is taken. First means, that if you sort that parts by their variant that the topmost variant is taken.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public MDPart GetPart( 
   string sPartNr
)
```
```

```
```
public:
MDPart^ GetPart( 
   String^ sPartNr
)
```
```

#### Parameters

*sPartNr*

Remarks

Returns null, if there is no part with that part number found in the database

Example

If the database contains the parts: "PartA"-"V4", "PartA"-"V1", "PartA"-"V2", "PartA"-"V3" than GetPart("PartA") returns "PartA"-"V1"

See Also

#### Reference

[MDPartsDatabase Class](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase.html)
  
[MDPartsDatabase Members](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase_members.html)
  
[Overload List](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetPart.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetPart(String))