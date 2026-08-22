# P501031: The general function definition '<x>' entered at the part should not be used at the part

### Cause

In the parts database to be checked a [part](Glossary_o_artikel.htm) was found where a "general" function definition is entered. The general [function definitions](Glossary_o_funktionsdefinitionen.htm) are intended to be used in [projects](Glossary_o_projekte.htm) if the exact parts are not yet clear when the project configuration is carried out. Only the exact function definitions should be entered in the parts management.

![](../Pictures/Gui/ALL/note.png)Note:

This message is only output for terminals.

### Solution

1. In the message management dialog mark the line with the message and select the Properties popup menu item.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The Parts management dialog is opened, the respective part is already marked in it.
2. Bring the Function templates tab to the front.
3. In the Device selection ([function templates](Glossary_o_funktionsschablonen.htm)) table click the entry in the Function definition column that contains the general function definition and click [...].
4. Select an exact function definition from the Function definitions dialog that is opened.
5. Close the parts management, save the modified data, and carry out a parts synchronization.
6. Then start a new check run.