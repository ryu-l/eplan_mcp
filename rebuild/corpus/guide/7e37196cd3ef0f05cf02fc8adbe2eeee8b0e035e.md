# Tab Display (device)

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have opened a project.

- You have inserted a symbol in the graphical editor or generated a new function in a navigator. In the Properties <...> dialog, select the Display tab.
- You have selected a function in the graphical editor or in a navigator. Tab Home > Command group Edit > Properties (or popup menu item Properties). In the Properties <...> dialog, select the Display tab.
- You have selected a placeholder object in the graphical editor or in a navigator. Tab Home > Command group Edit > Properties (or popup menu item Properties). In the Properties <...> dialog, select the Display tab.

In this tab you can specify the display settings for the different properties of the placed function / placeholder object. Individually placed properties can be docked with each other and made into a single block; when moving, this allows all the (desired) text to be moved at once and avoids overlapping of multi-line text with other text.

Overview of the main dialog elements:

Property arrangement:

In the drop-down list, different predefined assignment configurations are offered for selection. These configurations are stored on the symbol with their names.

From the drop-down list, select the desired property arrangement. It will specify the placed properties and their display settings, as well as the display settings for the connection points and the contact image. At the pre-defined arrangement configurations, there are already certain properties that have been selected for the display, and their values are specified in the right side of the dialog. Select "user-defined" if you want to specify your own arrangement. You can then save it under a new name by clicking the ![](../Pictures/Gui/ALL/all_save_as.png) (Save) button in the toolbar above the drop-down list or, if necessary, delete it again. The user-defined property arrangements apply only for symbol variants for which they were created and are therefore only available for components with the same symbol variants.

---

3D functions tab / Components tab

In the 3D functions tab, specify which properties are to be placed and displayed together with a 3D part placement. In the Components tab, specify which properties are to be placed and displayed together with a component. The properties chosen for display from the selected property arrangement will be listed in these tabs.

![](../Pictures/Gui/ALL/note.png)Note:

Whether the Connection points and / or Contact image tabs are to be shown additionally for a component depends on the respective symbol. This way the Connection points tab for symbols without connection points (for example black boxes, PLC boxes, cable definition lines) is not displayed.

The settings of the property arrangements have an effect on the placement of the DT and all other properties docked to it.

---

Tab Connection points

In the Connection points tab you have the option of editing the connection point property placements. The default here is that all connection point designations and descriptions of the symbol are displayed.

---

Contact image tab

In the Contact image tab you specify whether a contact image is displayed. To this purpose you select the alignment of the contact image via ![](../Pictures/Gui/ALL/all_new_as.png) (New) in the dialog Generate contact image:

- In path: The contact image â depending on the selected plot frame â is displayed below or right on the page in the schematic path of the component.
- On component: The contact image is displayed next to the component.

The settings for the contact image are saved at a property arrangement.

---

Property / Assignment:

As soon as you have selected a property in the 3D functions, Components or Connection points tab, you can edit its display properties in the table on the right-hand side of the dialog. To this purpose the hierarchy levels Format, Value / unit, Position and - for Components or Connection points - in addition the hierarchy levels Text box, Alignment box and Date / Time are available. These can be opened by clicking the ![](../Pictures/Gui/ALL/all_expand_hierarchy_as.png) sign.

To be able to edit the settings for the contact image in the Contact tab you must select one of the contact image alignments ("In path", "On component"). The hierarchy levels Position and Setting are available to this purpose.

The settings described in the following sections are available for the display properties:

- [Display Properties: Placed Property](devicetaggui_r_anzeigeeigenschaften.htm)
- [Display Properties: Contact Image](devicetaggui_r_anzeigekontaktspiegel.htm)

See also

[Dialog Save property arrangement](devicetaggui_d_eigschanordnungspeichern.htm)

[Tab Symbol / function data](devicetaggui_r_symbolfunktionsdaten.htm)

[Translating Project Texts](translategui_k_start.htm)

[Using User-Defined Property Arrangements](devicetaggui_h_eigschanordnungen.htm)