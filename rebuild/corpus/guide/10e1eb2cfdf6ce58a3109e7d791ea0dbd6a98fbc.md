# P026071: Missing tool at export (copper NC).  <x>

### Cause

The current tool list of the machine for the Export Copper NC does not contain the necessary tool. This is why the cut-out is not exported.

### Solution

1. Locate the cut-out in the layout space using the Go to (graphic) functionality from the popup menu in the Message management dialog.
2. Complete your tool list, or correct the cut-out.
3. Export the data again.

![](../Pictures/Gui/ALL/note.png)Note:

Using a new check run (any desired scheme) this module-specific message can be deleted from the message management dialog.