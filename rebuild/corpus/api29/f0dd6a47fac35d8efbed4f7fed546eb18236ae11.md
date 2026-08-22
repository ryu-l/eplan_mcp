# AddConstruction Method

AddConstruction Method

Adds a new construction to the parts database

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public MDConstruction AddConstruction( 
   string name
)
```
```

```
```
public:
MDConstruction^ AddConstruction( 
   String^ name
)
```
```

#### Parameters

*name*
:   The name of the construction will be added.

Exceptions

| Exception | Description |
| --- | --- |
|  | If construction already exists. |

Remarks

The name has to be unique in the construction list of the parts database.

See Also

#### Reference

[MDPartsDatabase Class](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase.html)
  
[MDPartsDatabase Members](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase_members.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~AddConstruction)