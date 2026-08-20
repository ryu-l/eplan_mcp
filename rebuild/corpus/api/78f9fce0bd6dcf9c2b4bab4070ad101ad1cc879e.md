# AddAccessoryPlacement Method

AddAccessoryPlacement Method

Adds a new accessory placement to the parts database

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public MDAccessoryPlacement AddAccessoryPlacement( 
   string name
)
```
```

```
```
public:
MDAccessoryPlacement^ AddAccessoryPlacement( 
   String^ name
)
```
```

#### Parameters

*name*
:   The name of the accessory placement that will be added.

Exceptions

| Exception | Description |
| --- | --- |
|  | If accessory placement already exists. |

Remarks

The name has to be unique in the accessory placement list of the parts database

See Also

#### Reference

[MDPartsDatabase Class](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase.html)
  
[MDPartsDatabase Members](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase_members.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)