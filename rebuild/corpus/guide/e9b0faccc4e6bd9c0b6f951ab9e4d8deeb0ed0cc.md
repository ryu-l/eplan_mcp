# P004122: The logical network '<x>' is connected via different bus systems

### Cause

Within a configuration project there are bus ports at which identical values at the properties Physical network: Name and Logical network: Name are entered. However, the bus ports are assigned to different bus systems.

### Solution

1. Locate the bus ports in the schematic by using the functionality Go to (graphic) and Go to 2nd coordinate, which the popup menu of the Message management dialog offers you.
2. Open the property dialog of the bus ports.
3. Bring the Bus data tab to the front.
4. Assign different names to all reported bus ports in the Logical network: Name field.
5. Confirm your entries.
6. If required, start a new check run.

![](../Pictures/Gui/ALL/note.png)Note:

This check run is "project-specific". This means that the check run is only performed if you have marked the project name in the page navigator or have selected the Apply to entire project check box in the Run check dialog.