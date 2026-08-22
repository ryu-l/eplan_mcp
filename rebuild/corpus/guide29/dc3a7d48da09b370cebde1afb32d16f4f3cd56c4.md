# P028011: PLC address at the planning object without placed PLC connection point

### Cause

There is no matching detail planning (placement in the schematic) for a PLC address assigned to a planning object.

### Solution

Create the detail planning:

1. Locate the PLC address and associated planning object in the pre-planning navigator using the Synchronize selection function offered by the popup menu in the Message management dialog.
2. Highlight the PLC address in the pre-planning navigator, place it on a schematic page using the Place popup menu item, and assign to it the same CPU address and the same symbolic address as in the pre-planning.
3. Then start a new check run.