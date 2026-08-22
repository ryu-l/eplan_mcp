# Changing the Length of Objects in the Layout Space

The length of variable-length items placed in the layout space can be modified subsequently. The length can always be changed only for an individual object; it is not possible to select several objects. Different forms of input can be used to define the new length:

- Free point entry by clicking
- Snapping a projection point to another object
- Entering a positive or negative value in the input box.

Preconditions:

- You have opened a project.
- You have opened the layout space navigator and a layout space.
- The layout space contains at least one variable-length item.

1. Select the following commands: Tab Edit > Command group Graphic > Change length.
2. Click the object to be changed on the end at which the change is to take place.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The object is displayed at the current cursor position. A red snap point appears on the cursor at the selected end. The end of the object that you clicked can be moved in both directions with the cursor. The 3D snap points of the mounting panel are displayed in blue; the snap points of the other components in the layout space appear as soon as the cursor touches them.

### [ClosedClicking to change length](javascript:void(0);)

1. Move the cursor to the position to which the object is to be extended or shortened.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The object representation follows the cursor.
2. Specify the new end point for the object.

### [ClosedChanging length by snapping a projection point](javascript:void(0);)

1. Move the cursor close to a displayed 3D snap point. The snap points on other objects of the same type appear if you move the cursor over them. The edges of mounting panels are also found without displaying a snap point.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The cursor snaps onto the snap point it finds or onto an edge. The red cursor snap point is surrounded by a red square.
2. Specify the new end point for the object.

### [ClosedChanging length by entry in the input box](javascript:void(0);)

1. Click the object to be changed on the end at which the change is to take place.
2. Enter the value by which the object is to be extended or shortened in the input box. Values without a preceding sign or values with a preceding "+" extend the box, while values with a preceding "-" shorten it.
3. Confirm the entered value.

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

Changing length by different forms of input and results

| **Form of input** | Input | Result |
| --- | --- | --- |
| Click |  |  |
| Projection point |  |  |
| Input box |  |  |

See also

[Fitting Length-variable Items](cabinetgui_h_einpassen.htm)

[Placing length-variable items](cabinetgui_h_varbtplatzieren.htm)