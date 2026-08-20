# ExecuteInMainThreadSync Method

ExecuteInMainThreadSync Method

Execute this work in a synchronous main thread.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public object ExecuteInMainThreadSync( 
   ExecuteInEplanMainThreadDelegate3 pExecuteDelegate,
   object x
)
```
```

```
```
public:
Object^ ExecuteInMainThreadSync( 
   ExecuteInEplanMainThreadDelegate3^ pExecuteDelegate,
   Object^ x
)
```
```

#### Parameters

*pExecuteDelegate*
:   The work to be done.

*x*

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when no MainThreadDispatcher was set. |

See Also

#### Reference

[EplanMainThreadDispatcher Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Internal.EplanMainThreadDispatcher.html)
  
[EplanMainThreadDispatcher Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Internal.EplanMainThreadDispatcher_members.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)