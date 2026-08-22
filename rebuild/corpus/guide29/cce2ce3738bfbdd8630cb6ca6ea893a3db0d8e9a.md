# P004107: Address range of the PLC card '<x>' overlaps with the address range of the PLC card '<y>'

### Cause

The address areas of two [PLC boxes](Glossary_o_sps_kaesten.htm) are defined in such a way that their address areas overlap.

### Solution

1. Locate the PLC boxes of the [PLC cards](Glossary_o_sps_karten.htm) in the schematic via the popup menu of the Message management dialog. Use the Go to (graphic) functionality to jump to the PLC card '<x>'. Use the Go to 2nd coordinate functionality to jump to the PLC card '<y>'.
2. Call up the [property dialog](Glossary_o_eigenschaftendialog.htm) of both PLC boxes and in the process bring the first tab to the front.
3. In the [properties](Glossary_o_eigenschaften.htm) list adjust the values of the fields Start address of PLC card and PLC device: Data length (...) accordingly in such a way that an overlap of the address areas of both PLC cards is impossible.
4. Confirm your entries.
5. Then start a new check run.

![](../Pictures/Gui/ALL/note.png)Notes:

This check run checks whether the address areas of PLC cards overlap.

In the process the following information is considered:

- The PLC-specific setting Separate address range for inputs and outputs.
- The association of the PLC card and CPU. To this purpose only the CPU: Name ([ID](Glossary_o_id.htm) 20253) property is taken into consideration. This means that a PLC card can only belong to one CPU.

Both the PLC card as well as the associated PLC subdevices are checked for the overlap of address areas.

The following conditions must be met so that the check run can be executed:

- An associated PLC box with the properties Start address of PLC card and PLC device: Data length exists. The corresponding fields must be filled with a value.
- The CPU: Name (ID 20253) property may not be empty. This entry determines the address scheme to be used.
- In the PLC-specific [settings](Glossary_o_einstellungen.htm) of the address scheme belonging to the CPU a counter with the configuration value "Start address of PLC card" must be defined.

In addition the following applies for the check run:

- Without specification of an addressing scheme the address range (to = "start address + data length") cannot be calculated.
- The data length is specified independent of the addressing scheme used as decimal value in bits.
- The data length can be stored in the parts management and applied from there.