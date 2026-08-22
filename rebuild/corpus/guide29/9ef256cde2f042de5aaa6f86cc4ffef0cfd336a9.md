# Action: XGedUpdateMacroAction

This action updates [macros](Glossary_o_makros.htm). Using the ProjectName parameter, you can transfer the complete file path of a project. If the project in question is not open, it will be opened automatically by this action and then closed again. If no project has been specified, the action will be executed for the object selected in the graphical editor. In order for a macro to be updated in such a case, the selected object must be a macro box or an object assigned to the macro box.

  

|  |  |
| --- | --- |
| **Parameters** | **Description** |
| ProjectName | Project name with complete file path (optional). If the project in question is not open, it will be opened automatically by this action and then closed again. |
| AutoAssignLastUsedRecord | Automatically assigns the last value set used to several placeholders (optional). |

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

```
XGedUpdateMacroAction 
/ProjectName:"C:\myFolder\MyProject.elk"
```