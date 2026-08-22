# Tab Structure (Changing Standards)

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have opened a project. In the case of several opened projects: You have selected a project in the page navigator. Tab Tools > Command group Standards > Exchange. You have specified all of the settings in the Project tab. Button [Next]. You have specified all of the settings in the Rotation / flipping tab. Button [Next]. You selected the check box in the Master data tab in a symbol library row in the Individual assignment column. Button [Next]. You have specified all of the settings in the Symbols tab. Button [Next].

This tab displays the project structure from the template and transfers it to the target project. You can adjust the project structure in this tab.

Overview of the main dialog elements:

Pages:

This drop-down list shows all user-defined and pre-defined schemes for the page structure. Select a scheme to define the page structure. Click [...] to open the Page structure dialog, where you can create, edit, and manage schemes.

General devices ... Mechanical devices:

This drop-down list shows all user-defined and pre-defined identifier schemes for the respective device. This is used to select an identifier scheme to define the device structure for the devices. Click [...] to open the Device structure dialog, where you can create, edit, and manage schemes.

Superior:

You can select this check box for terminal strips, plugs, cables, and / or interruption points. It is only available when you have selected an identifier scheme with identifying or describing identifier blocks. If the check box is checked, devices without a "â" preceding sign in the DT are treated in the same way as sequentially-numbered devices. The full DT then contains no identifier block of the project structure.

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

DT with preceding sign

| Displayed DT | Result |
| --- | --- |
| -X3 | Z1+A1-X3 |

DT without preceding sign

| Displayed DT | Result |
| --- | --- |
| X3 | X3 |

![](../Pictures/Gui/ALL/note.png)Note:

Please note that the Superior setting has been discontinued and will not be supported in future. This check box is only still displayed if you have already used the Superior setting in a project or if you activate the setting Allow structure setting 'Superior' that is not norm-compliant in the dialog Settings: Compatibility (command path: File > Settings > Projects > "Project name" > Management > Compatibility).

[Other]:

Opens the Extended project structures dialog. Allows the definition of preceding signs and classification points for identifier blocks.

See also

[Project Structure](projectstructure_k_start.htm)

[Project Structure: Basics](projectstructure_k_hinterg.htm)

[Defining the Project Structure](changestandardsgui_h_projektstrukturanpassen.htm)