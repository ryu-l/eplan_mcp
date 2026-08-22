# P005068: Connection (3D mounting layout) with connection point that is not defined in the connection point pattern

### Cause

There exists in a [layout space](Glossary_o_bauraum.htm) a connection of the "3D mounting layout" representation type whose connected source or whose connected target has a connection point designation that is not defined in the connection point pattern.

### Solution

1. Locate the connection of the "3D mounting layout" representation type in the layout space using the Go to (graphic) functionality from the popup menu in the Message management dialog.
2. Follow the connection in the layout space both up to the connected source and the connected target.
3. Check the connection point pattern at the source and target by calling up the Properties <...> dialog of [part](Glossary_o_artikel.htm) placement and bringing the Connection point pattern tab to the front.
4. There, you delete the connection point designation that is not part of the connection point pattern, and close the Properties <...> dialog by clicking [OK].
5. Then start a new check run.

![](../Pictures/Gui/ALL/note.png)Note:

The check run is also output if the connection point has been defined in the connection point pattern and all values in the columns for the X, Y, and Z position are set to "0".

In this case, enter a value other than "0" for at least one position of the connection point.