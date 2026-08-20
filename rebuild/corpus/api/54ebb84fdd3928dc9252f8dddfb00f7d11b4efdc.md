# IWriteProtection Interface

IWriteProtection Interface

Defines methods to manipulate write protection on object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public interface IWriteProtection
```
```

```
```
public interface class IWriteProtection
```
```

Example

The following example shows how to use the interface.

- [C#](#i-tab-content-f3054936-0578-4baf-a541-a755c3db1798)

```
oFunction.Properties.HARNESS_NAME = "old value";
oFunction.WriteProtected = true;
using (UndoStep oUndoStep = new UndoManager().CreateUndoStep())
{
    oFunction.Properties.HARNESS_NAME = "new value";
}
Console.WriteLine(oFunction.Properties.HARNESS_NAME.ToString());  //will be 'old value' returned
```

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [WriteProtected](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IWriteProtection~WriteProtected.html) | Checks if an object is currently write protected or sets manual write protection |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [GetWriteProtectionFlagSet](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IWriteProtection~GetWriteProtectionFlagSet.html) | Checks what kind of a write protection was set. |
| Method | [PauseWriteProtection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IWriteProtection~PauseWriteProtection.html) | Temporarily disables write protection. Note that current write protection flags are not cleared. |

[Top](#top)

See Also

#### Reference

[IWriteProtection Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IWriteProtection_members.html)
  
[Eplan.EplApi.DataModel Namespace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel_namespace.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)