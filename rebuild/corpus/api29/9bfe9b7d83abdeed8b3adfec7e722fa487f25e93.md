# AddMenuItem Method (ContextMenu)

AddMenuItem Method (ContextMenu)

Adds a new menu item at the end of a context menu.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool AddMenuItem( 
   ContextMenuLocation contextMenuLocation,
   string strMenuName,
   string strActionName,
   bool bSeparatorBefore,
   bool bSeparatorBehind
)
```
```

```
```
public:
bool AddMenuItem( 
   ContextMenuLocation^ contextMenuLocation,
   String^ strMenuName,
   String^ strActionName,
   bool bSeparatorBefore,
   bool bSeparatorBehind
)
```
```

#### Parameters

*contextMenuLocation*
:   This is the identifier of the context menu where the new menu should inserted at.

*strMenuName*
:   The name of the menu to be added.

*strActionName*
:   Name of the [Eplan.EplApi.ApplicationFramework.Action](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action.html) to be performed when the menu item is selected. Also its parameters can be passed here.

*bSeparatorBefore*
:   when true, a new separator is added before the menu item is added.

*bSeparatorBehind*
:   when true, a new separator is added behind the new menu item.

#### Return Value

true when an item was added. Returns false when this menu item already exists.

See Also

#### Reference

[ContextMenu Class](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.ContextMenu.html)
  
[ContextMenu Members](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.ContextMenu_members.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.Guiu~Eplan.EplApi.Gui.ContextMenu~AddMenuItem)