# P005053: Unconnected connection point at terminal

### Cause

An unconnected symbol connection point was identified at a terminal in the schematic. The message also appears if the terminal has multiple symbol [connection points](Glossary_o_anschluesse.htm), only one of which is connected to a [component](Glossary_o_schaltzeichen.htm).

### Solution

1. Locate the relevant terminal in the schematic using the Go to (graphic) function from the popup menu in the Message management dialog.
2. Connect all open symbol connection points with a component so as to [form](Glossary_o_verlauf.htm) [autoconnecting](Glossary_o_autoconnecting.htm) [lines](Glossary_o_leitungen.htm).
3. Or, if the terminal is no longer needed, delete it from the schematic.
4. Then start a new check run.