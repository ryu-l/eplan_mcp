# P004114: PLC address '<x>' is not located in the address range of the subdevice '<y>' belonging to the PLC card

### Cause

At a PLC connection point an address was defined that does not lie within the address range of the subdevice associated with the PLC card.

PLC connection points with the "PLC connection point, internal, general" function definition are not checked since they are only used for the display of free symbolic addresses.

### Solution

1. Locate the PLC connection point in the schematic using the Go to (graphic) functionality that is provided by the popup menu of the Message management dialog.
2. Call up the property dialog of the PLC connection point.
3. At the PLC connection point determine the values entered in the first tab for the properties Address and PLC subdevice: Index (property list).
4. Jump via the popup menu item Go to (counterpiece) of the PLC connection point to the associated PLC box of the PLC card.
5. Launch the property dialog of the PLC box.
6. Determine the values entered in the property table of the first tab in the field PLC Subdevice (X): Start address (...) and PLC Subdevice (x): Data length (...).
7. Change either the PLC address of the PLC connection point so that it is located within the address range of the PLC card, or modify the start address or the data length for the subdevice accordingly at the PLC box.
8. Confirm your entries.
9. If required, start a new check run.