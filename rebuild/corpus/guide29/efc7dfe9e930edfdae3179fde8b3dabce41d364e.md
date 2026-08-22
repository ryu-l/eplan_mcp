# P004009: Slot (module) '<x>' of a rack '<y>' assigned several times

### Cause

For several [PLC boxes](Glossary_o_sps_kaesten.htm) with bus data for the same [rack](Glossary_o_baugruppentraeger.htm) and configuration project, you also entered the same slot positions.

### Solution

1. Open the Properties <...> dialog for the corresponding PLC boxes.
2. In the PLC structure data tab, enter different values for each of the Position (slot / module) fields.
3. Then start a new check run.

![](../Pictures/Gui/ALL/note.png)Notes:

- This check run only checks PLC boxes at which a configuration project is entered.
- During this check the property PLC card is placed on head station is also considered. This message is not output if of two [PLC cards](Glossary_o_sps_karten.htm) that have the same slot number one is placed on the rack and the other on the head station. The property PLC card is placed on rack [ID](Glossary_o_id.htm) means lateral extension, the property PLC card is placed on head station means upward extension.