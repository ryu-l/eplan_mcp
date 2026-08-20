# Action: XDLInsertDeviceAction

|  |  |
| --- | --- |
| **Parameters** | **Description** |
| PartNr | Part number |
| PartVariant | Part variant |
| ProjectId | Project ID |
| PropertyIndex | Index of the project parts, must be reduced to 1-50. If PropertyIndex = 0, no project part will be displayed. |

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

```
XDLInsertDeviceAction 
/PartNr:MOE.010042 
/PartVariant:1 
/PropertyIndex:0 
/ProjectId:0
```