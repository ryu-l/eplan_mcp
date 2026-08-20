# Tab Settings (macro box)

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have inserted a macro box in a macro project (Tab Master data > Command group Macros > Drop-down button Navigator > Insert macro box), or you have double-clicked an existing macro box. In the Properties <...> dialog, select the Settings tab.

This tab shows you the settings for the macro box. In a Macro project you specify - depending on the respective specified type of usage in the [Macro box](macrosgui_r_makrokasten.htm) tab - different settings that should be considered when inserting the generated macro. In a Schematic project you can only make settings for the handle

Overview of the main dialog elements:

Generate protected group during insertion:

Activate this check box if a protected group is to be generated during insertion of the macro. Such a group offers a graphical protection. This means the properties of the macro components can be edited but the macro itself cannot be changed graphically or further broken down.

Also insert macro box:

Use the drop-down list to specify if you want the macro box to be inserted as well when inserting the generated macro. This setting is also taken into consideration when inserting a device, if a macro is stored for this device.

If you select the "From project settings" entry in this field, the project-wide setting [Also insert macro boxes](gedviewer_d_einstellungenprojektallgemein.htm) is used.

Take connection point designations into account:

By means of this drop-down list you specify whether the connection point designations also have to be identical in addition to the function definitions of the functions for the device assignment. This, for example, has the effect that the matching functions from the stored macro are assigned during the placement of complex devices.

This setting is also used when updating macros. If the value is set to "Yes" here, the connection point designations are transferred during the update from the macro files to the inserted macros in the schematic. If the value is set to "No", the connection point designations of the macros in the schematic are retained during the update.

If you select the "From user settings" entry in this field, the user-specific setting [Take the connection point designations into account during the device assignment](xessettingsgui_d_betriebsmittelallgemeinbenutzer.htm#GeraetezuordnungMitAnschluessen) is used.

![](../Pictures/Gui/ALL/note.png)Note:

The [Keep DT only](gedviewer_d_einstellungenmakrosaktualisieren.htm#BMKBeibehalten) setting for updating macros takes priority over the settings for taking the connection point designations into account. If this setting is activated for updating, all connection point designations as well as all other logical data with the exception of DT is transferred from the macro file to the functions of the macros in the schematic - even if the setting Take connection point designations into account is set to the value "No".

---

Group box Handle

The handle is defined as the point where the cursor "sticks" when the macro is inserted. Normally, the macro hangs at the "top, left" on the first insertion point.

Active:

If this check box is selected, the default handle position is displayed and you can change it. The X and Y position fields are enabled and you can overwrite the default values. After closing the dialog with [OK] the handle position is indicated on the page with a special graphical symbol.

If the check box is deactivated, no entries can be made in the X and Y position fields and the handle is also no longer displayed. If you reselect the check box the handle is reset to its default position.

X position / Y position:

If the Active check box is selected, the default values for the handle position are first displayed here. You cannot change these values.

See also

[Macros: Protected Groups](macrosgui_k_geschuetztegruppen.htm)

[Using Macro Boxes](macrosgui_h_makrokasten.htm)