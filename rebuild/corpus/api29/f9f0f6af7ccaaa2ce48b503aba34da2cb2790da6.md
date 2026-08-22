# IsActionEnabled Method

IsActionEnabled Method

Get the enabled/disabled state of a action in a menu (or/and on a toolbar)

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool IsActionEnabled( 
   string strNameOfAction
)
```
```

```
```
public:
bool IsActionEnabled( 
   String^ strNameOfAction
)
```
```

#### Parameters

*strNameOfAction*
:   the name of the action (optional: with some parameters)

#### Return Value

true when the action is enabled

Example

- [C#](#i-tab-content-7a437a24-1c33-4975-8245-874375e6b573)

```
Eplan.EplApi.Gui.Menu theMenuToCheck = new Eplan.EplApi.Gui.Menu();
bool bIsEnabled = theMenuToCheck.IsActionEnabled("CustomAction1 /Parameter1:Value1");
```

See Also

#### Reference

[Menu Class](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.Menu.html)
  
[Menu Members](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.Menu_members.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.Guiu~Eplan.EplApi.Gui.Menu~IsActionEnabled)