# P007001: The device uses more functions than provided by the associated part

### Cause

You added another function to a device that you placed as a part with fixed function templates (device), and assigned the device DT to it. The part cannot use this kind of function supplement.

### Solution

#### Possibility 1

Select a part with the corresponding function templates.

#### Possibility 2

Extend the function template settings for the selected part in the parts management.

1. Select the following commands: Tab Master data > Command group Parts > Management.
2. In the Parts management dialog, select the Function templates tab.
3. Click ![](../Pictures/Gui/ALL/all_new_as.png) (New) above the table. A new row is added.
4. Click in the cell of the first column and then click [...].
5. In the Function definitions dialog select the function you want, to extend the part.
6. Confirm your selection by clicking [OK], and copy the changed setting into the parts management.
7. Then place the device in the schematic once again.

---

  

If required, start a new check run.

![](../Pictures/Gui/ALL/note.png)Note:

The message is also output at the following situation: You have identified a function as a safety function at a device. However, the associated function template is not defined as a safety function at the selected part. You can avoid the messages by activating the check box at the associated function template for the selected parts in the Parts management, Function templates tab.