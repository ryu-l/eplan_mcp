# P007015: The macro stored at the first part does not correspond to the one belonging to this main function

### Cause

This message is displayed in conjunction with [macro boxes](Glossary_o_makrokaesten.htm) if the following conditions are met:

- A macro, limited by a macro box, contains several [functions](Glossary_o_funktionen.htm) that are assigned to the macro box.
- A parts data assignment for at least one property exists in the macro box.
- For the main function, a [part](Glossary_o_artikel.htm) to which a macro is assigned was selected at the first part position. The macro names of the part and the macro box are different.

### Solution

Assign a part that has the same macro name as the macro box to the main function in the macro box at the first part position. The two macro names must match.

Then start a new check run.