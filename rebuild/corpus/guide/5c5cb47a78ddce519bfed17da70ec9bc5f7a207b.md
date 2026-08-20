# P004082: Configuration project '<x>' does not contain a CPU

### Cause

The information that a PLC box is a CPU is missing at a PLC box. This information is required for a correct PLC data export from Eplan.

This check run only checks PLC boxes which are main functions and at which a configuration project is entered.

![](../Pictures/Gui/ALL/note.png)Note:

The data exchange is also allowed with subprojects. It is possible that a part project does not contain a CPU, even if a CPU is contained in the full project.

### Solution

1. Locate the PLC box in the schematic using the Go to (graphic) functionality that is provided by the popup menu of the Message management dialog.
2. Open the property dialog of the PLC box.
3. Bring the PLC structure data tab to the front.
4. Activate the CPU check box in the properties table.
5. Ensure that a configuration project and a station ID are entered at the PLC box.
6. Click [OK].
7. If required, start a new check run.

![](../Pictures/Gui/ALL/note.png)Note:

Note that a CPU does not have to exist at each station. It is sufficient if at least one CPU exists among all the stations that are assigned to a configuration project.