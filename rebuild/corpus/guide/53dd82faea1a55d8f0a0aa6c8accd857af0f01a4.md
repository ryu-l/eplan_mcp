# P003029: For cable connection '<x>' the connected pin '<y>' of the prefabricated cable is not specified as the conductor start or conductor end

### Cause

A prefabricated cable was determined in the project whose cable connections are not connected to the correct pins.

### Solution

1. Double-click the line with the message in the dialog Message management to locate the respective cable in the schematic.
2. Double-click the cable in the schematic and in the dialog Properties bring the Parts tab to the foreground.
3. Look up the part in question and close the dialog.
4. Select the following commands: Tab Master data > Command group Parts > Management.
5. In the dialog Parts management search for the determined cable part and bring the Function templates tab to the foreground.
6. Look up which pins are assigned to the individual cable connections of the cable and close the parts management. Compare this assignment with the connected pins in the schematic.

![](../Pictures/Gui/ALL/note.png)Note:

The pin assignment is defined for each cable connection via the properties Conductor start and Conductor end. The assignment is possible, for example, via the item numbers of the function templates. The values stored here correspond to the item numbers of the pins within the table on this tab.  
A further possibility is the assignment via the specification of the subordinate DT and the pin designation (for example "X1:2") or via the specification of the DT ID and the pin designation (for example "ID:X1:2").

7. Ensure that the correct connections are connected to the pins in the schematic. To do so move the pins to the matching connections depending on the concrete error. Or change the connection properties, for example by exchanging the connection definition points.
8. If required, start a new check run.