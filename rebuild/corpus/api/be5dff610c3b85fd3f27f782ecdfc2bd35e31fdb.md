# Terminal.TerminalStripCache Class

Terminal.TerminalStripCache Class

This class is used to enhance performance when getting sub-terminals of multi-level terminals. In order to enhance performance, create an object of this class before accessing sub-terminals of subsequent multi-level terminals and delete it afterwards.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.EObjects.Terminal.TerminalStripCache**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public sealed class Terminal.TerminalStripCache
```
```

```
```
public ref class Terminal.TerminalStripCache sealed
```
```

Example

Example of usage

- [C#](#i-tab-content-962236be-18b4-423d-9e67-2db0fd9cc63f)

```
Terminal[] oTerminals = new DMObjectsFinder(m_DistributedTerminalsProject).GetTerminals(null);
using (Terminal.TerminalStripCache oCache = new Terminal.TerminalStripCache())
{
    foreach (Terminal oTerminal in oTerminals)
    {
        StorableObject oParent = oTerminal.ParentFunction;
    }
}
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Terminal.TerminalStripCache Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+TerminalStripCache~_ctor.html) | Constructor |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+TerminalStripCache~Dispose().html) | Deterministic finalizer |

[Top](#top)

See Also

#### Reference

[Terminal.TerminalStripCache Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+TerminalStripCache_members.html)
  
[Eplan.EplApi.DataModel.EObjects Namespace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects_namespace.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)