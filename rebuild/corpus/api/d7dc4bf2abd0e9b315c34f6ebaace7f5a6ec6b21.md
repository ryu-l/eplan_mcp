# EventHandlerWrapper Class

EventHandlerWrapper Class

Event handler to process Eplan events in a remoting client. It is not possible to directly use the [EventHandler](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler.html) in a remoting client!

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.ApplicationFramework.EventHandlerWrapper**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public class EventHandlerWrapper
```
```

```
```
public ref class EventHandlerWrapper
```
```

Example

Response to Eplan events in a remoting client

- [C#](#i-tab-content-0eb513e1-e7e8-440a-a20a-b5b44c3e96b4)

```
Eplan.EplApi.ApplicationFramework.EventHandler oEventHandler = new Eplan.EplApi.ApplicationFramework.EventHandler();
oEventHandler.SetEvent("onActionStart.String.*");
       
Eplan.EplApi.ApplicationFramework.EventHandlerWrapper oWrapper= new Eplan.EplApi.ApplicationFramework.EventHandlerWrapper();
oWrapper.EplanEventLocally += new Eplan.EplApi.ApplicationFramework.EventHandlerFunction(oWrapper_EventHandlerFunctionLocally);
          
oEventHandler.EplanEvent += new Eplan.EplApi.ApplicationFramework.EventHandlerFunction(oWrapper.LocallyEventHandlerFunction);
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [EventHandlerWrapper Constructor](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandlerWrapper~_ctor.html) |  |

[Top](#top)

Public Fields

|  | Name | Description |
| --- | --- | --- |
| Public Field | [EplanEventLocally](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandlerWrapper~EplanEventLocally.html) | Local event handler |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [InitializeLifetimeService](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandlerWrapper~InitializeLifetimeService.html) | This object should live "forever." |
| Public Method | [LocallyEventHandlerFunction](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandlerWrapper~LocallyEventHandlerFunction.html) | This function of the local event handler is registered as a handler function of the remote event handler [EventHandler](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandler.html). |

[Top](#top)

See Also

#### Reference

[EventHandlerWrapper Members](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.EventHandlerWrapper_members.html)
  
[Eplan.EplApi.ApplicationFramework Namespace](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework_namespace.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)