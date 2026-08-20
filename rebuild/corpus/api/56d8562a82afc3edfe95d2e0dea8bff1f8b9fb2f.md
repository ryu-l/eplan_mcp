# PauseWriteProtection Method (Connection)

PauseWriteProtection Method (Connection)

Temporarily disables write protection. Note that current write protection flags are not cleared.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual void PauseWriteProtection( 
   bool bPause
)
```
```

```
```
public:
virtual void PauseWriteProtection( 
   bool bPause
)
```
```

#### Parameters

*bPause*

Exceptions

| Exception | Description |
| --- | --- |
| [WriteProtectionNotSet](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.WriteProtectionNotSet.html) | Thrown if object has no write protectection. |

See Also

#### Reference

[Connection Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)
  
[Connection Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection_members.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)