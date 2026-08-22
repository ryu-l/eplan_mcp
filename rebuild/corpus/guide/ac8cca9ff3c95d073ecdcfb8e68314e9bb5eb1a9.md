# P026052: Source / Target is not placed

### Cause

A part placement that is the source or target of a routing connection has been removed from the layout space or has not been placed there. This means that the source and/or the target of the routing connection are not placed in the same layout space.

### Solution

#### Possibility 1

Place the unplaced source and / or the unplaced target of the routing connection from the 3D mounting layout navigator in the layout space.

#### Possibility 2

If you want the part placement that does not exist in the layout space to be the source or target of the routing connection outside of the enclosure, it must be marked as an external placement:

1. Locate in the schematic the part not placed in the layout space. To this purpose use the Go to (graphic) functionality from the popup menu in the Message management dialog.
2. Call up the dialog Properties <...> of the associated device.
3. Bring the Part tab to the front, and select the Part reference data category in the right-hand section of the tab.
4. In the list activate the External placement check box.
5. Click [OK].

---

  

Route the connections again.

![](../Pictures/Gui/ALL/note.png)Note:

Using a new check run (any desired scheme) this module-specific message can be deleted from the message management dialog.