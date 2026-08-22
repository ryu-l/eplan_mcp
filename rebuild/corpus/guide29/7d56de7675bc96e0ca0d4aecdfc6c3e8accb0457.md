# P026016: Device exists on the mounting surface without representation in the schematic

### Cause

The main function of a device that is located on a mounting surface as a [part](Glossary_o_artikel.htm) placement is missing from the schematic.

![](../Pictures/Gui/ALL/note.png) Note:

Main [functions](Glossary_o_funktionen.htm) that are assigned to the "Mechanics" trade are not affected.

### Solution

1. Place the missing main function of the device in the schematic retrospectively, and assign it the same displayed DT as the associated part placement on the mounting surface.
2. Then start a new check run.