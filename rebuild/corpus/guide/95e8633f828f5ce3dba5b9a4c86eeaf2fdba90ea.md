# P001030: Used distributed terminal connection point without connection point designation

### Cause

A distributed terminal connection point to which a function is connected, has no connection point designation.

![](../Pictures/Gui/ALL/note.png)Note:

Distributed terminal connection points that are connected by means of saddle jumpers, internal jumpers or direct connections do not require a connection point designation and are therefore not checked.

### Solution

1. Locate the distributed terminal in the schematic by using the Go to (graphic) functionality from the popup menu in the Message management dialog.
2. Open the Properties dialog of the distributed terminal and add the missing connection point designation in the field by the same name in the Terminal tab.
3. If required, start a new check run.