# Adding menu points by a script

Adding menu points by a script

A script can add one or more menu points to the utilities menu of EPLAN. When the script is loaded and if there is a function with the [DeclareMenu] attribute, the menu points specified by the Eplan.EplApi.Gui.Menu.AddMenuItem() function will be created.

A menu point is always connected with an action, which is called, when the menu item is clicked. This means the script either additionally registers an action, or the menu point is assigned to an already existing action.

Remarks

Please mind, that users may start EPLAN in QUIET mode using W3u.exe /Quiet or the API could be initialized by an [offline program](UsingEplanAssemblies.html). Because of this, it is not recommended to show any message boxes in the method marked by <DeclareMenu()>. If you encounter some problem during registering or initializing an script, just create and throw a BaseException or use BaseException.FixMessage(...) to add the message to the system messages list.

The following example shows a script, which registers an action and a menu point.

- [C#](#i-tab-content-CS)
- [VB](#i-tab-content-VB)

```
public class RegisterScriptMenu
{
    [DeclareAction("MyScriptActionWithMenu")]
    public void MyFunctionAsAction()
    {
       new Decider().Decide(EnumDecisionType.eOkDecision, "MyFunctionAsAction was called!", "RegisterScriptMenu", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
       return;
    }

    [DeclareMenu]
    public void MenuFunction()
    {
        Eplan.EplApi.Gui.Menu oMenu = new Eplan.EplApi.Gui.Menu();
        oMenu.AddMenuItem("MyMenuText", "MyScriptActionWithMenu");
    }
}
```

```
Public Class RegisterScriptMenu

   <DeclareAction("MyScriptActionWithMenu")>  _
   Public Sub MyFunctionAsAction()
      Dim dec As Decider = New Decider
      dec.Decide(EnumDecisionType.eOkDecision, "MyFunctionAsAction was called!", "RegisterScriptMenu", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)
      Return
   End Sub 'MyFunctionAsAction

   <DeclareMenu()>  _
   Public Sub MenuFunction()
      Dim oMenu As New Eplan.EplApi.Gui.Menu()
      oMenu.AddMenuItem("MyMenuText", "MyScriptActionWithMenu")
   End Sub 'MenuFunction
End Class 'RegisterScriptMenu
```

By the [DeclareMenu] attribute the function MenuFunction() will be called, when new menu points are to be registered in EPLAN. The function AddMenuItem() from the class Eplan.EplApi.Gui.Menu creates a new menu point "MyMenuText" and connects it to the action "MyScriptActionWithMenu".

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: script_menu)