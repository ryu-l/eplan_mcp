# CreateMergedConnections Method

CreateMergedConnections Method

Returns an array of MergedConnection objects created from the connections passed in the array parameter. connections that belong to representing the same corresponding connections with different placement types are merged together into one merged connection in the output vector.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public static MergedConnection[] CreateMergedConnections( 
   Connection[] connections
)
```
```

```
```
public:
static array<MergedConnection^>^ CreateMergedConnections( 
   array<Connection^>^ connections
)
```
```

#### Parameters

*connections*

#### Return Value

An array of merged connections for the given connections.

See Also

#### Reference

[MergedConnection Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedConnection.html)
  
[MergedConnection Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedConnection_members.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedConnection~CreateMergedConnections)