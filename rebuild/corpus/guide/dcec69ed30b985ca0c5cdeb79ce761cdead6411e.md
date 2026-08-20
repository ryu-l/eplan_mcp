# Creating and Inserting Pre-planning Macros

Any substructure of pre-planning (that is, associated structure segments and planning objects) can be stored in a pre-planning macro. Such a macro is a separate file type with the file name extension \*.emv. Pre-planning macros do not contain graphics, and can be created and inserted only in the pre-planning navigator.

### Creating pre-planning macros

Precondition:

You have opened a project that contains the pre-planning data, and have the pre-planning navigator open.

1. Highlight a structure segment or planning object in the pre-planning navigator.
2. Select the Create pre-planning macro popup menu item.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The Save as dialog is opened. In the Directory field, the default target directory is displayed.
3. In the File name field, enter the name of the macro. Click [...] to select another name and / or another target directory.
4. If desired, enter a description of the macro into the Description field. The text entered here is displayed in a comments field when inserting macros and simplifies the selection for you.  
     
   ![](../Pictures/Gui/ALL/arrow.png) All other fields are not available for pre-planning macros and are grayed out.
5. Click [OK].  
     
   ![](../Pictures/Gui/ALL/arrow.png) The macro is saved in the specified directory under the name <Name>.emv. Eplan checks whether a pre-planning macro already exists under the specified name. If so, you will be requested to decide whether the old macro is to be overwritten or not.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The pre-planning macro contains the highlighted structure segment or planning object, as well as the complete subordinate structure.

### Inserting pre-planning macros

Precondition:

You have opened a project, and have the pre-planning navigator open.

![](../Pictures/Gui/ALL/note.png)Note:

Pre-planning macros containing structure segments cannot be inserted below planning objects.

1. Select a structure segment in the pre-planning navigator.
2. Select the Insert pre-planning macro popup menu item.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The Select pre-planning macro dialog is opened.
3. Select the required pre-planning macro, and click [Open].   
     
   ![](../Pictures/Gui/ALL/arrow.png) The pre-planning macro is inserted below the marked structure segment.

See also

[Pre-planning: Principle](planninggui_k_prinzip.htm)