# Action: XCCreateGravingtextAction

|  |  |
| --- | --- |
| **Parameter** | **Description** |
| Complete | Keep location designations of the same name (optional, 0 = No, 1 = Yes). The action XCCreateGravingtextAction generates an engraving text from the DTs of the source and target of the cable. Without specification of a parameter or with specification of the parameter /Complete:0 the designation is shortened in accordance with the VASS standard (Volkswagen Audi Seat Skoda), meaning that structure identifiers of source and target having the same name are removed - starting from the left. Use the parameter /Complete:1 to retain location designations of the source and target that have the same name. |

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

```
XCCreateGravingtextAction 
/Complete:1
```