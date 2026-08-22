# GetButtonAction Method

GetButtonAction Method

returns the action for a button in this toolbar. When this button has a persistent button id, the buton has no Action but simple the persistent id. When this is a button added by the customer, the action is not empty.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public string GetButtonAction( 
   string strToolbarName,
   int nIndex
)
```
```

```
```
public:
String^ GetButtonAction( 
   String^ strToolbarName,
   int nIndex
)
```
```

#### Parameters

*strToolbarName*
:   the name of the toolbar.

*nIndex*
:   the index of the button. Starts with zero.

See Also

#### Reference

[Toolbar Class](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.Toolbar.html)
  
[Toolbar Members](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.Toolbar_members.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.Guiu~Eplan.EplApi.Gui.Toolbar~GetButtonAction)