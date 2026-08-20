# GetEnabled Method

GetEnabled Method

Returns whether an action is enabled

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool GetEnabled( 
   ActionCallingContext oCallingContext,
   string strActionWithParameters
)
```
```

```
```
public:
bool GetEnabled( 
   ActionCallingContext^ oCallingContext,
   String^ strActionWithParameters
)
```
```

#### Parameters

*oCallingContext*
:   Used to pass parameters to an action and to receive return values of the action

*strActionWithParameters*
:   Action name with parameters

Remarks

Is used to enable/dissable control bound to the action (usually RibbonCommand)

See Also

#### Reference

[Action Class](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action.html)
  
[Action Members](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action_members.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)