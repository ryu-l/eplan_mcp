# Tab Macro

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have opened a project.

- You have generated a planning object in the pre-planning navigator, or inserted one in the graphical editor. In the Properties <...> dialog, select the Macro tab.
- You have highlighted a planning object in the pre-planning navigator or in the graphical editor. Popup menu item Properties. Select the Macro tab.

Use this tab to assign to a planning object a macro file with window or page macros. If the macro contains placeholder objects, the placeholder objects and variables are displayed here, and you can edit the values of the placeholder objects. These values will be used when placing the macro.

Overview of the main dialog elements:

Macro:

The macro name is shown here. Click [...] to open the macro selection and select a macro.

Variant:

Only available for window macros. Select the desired variant of a window macro here. This way only the placeholder objects, variables and values of this variant are displayed in the Properties group box. If the macro variant has only one representation type, the selection dialog for placing macros is no longer required when planning objects are dragged into the page navigator via Drag & Drop in order to generate schematic pages.

If the macro originates from the assigned [segment template](planninggui_r_planungsobjekt.htm#Segmentvorlage), the macro name displayed in the Macro field cannot be changed. However, the selection of a different variant is possible in such a case.

![](../Pictures/Gui/ALL/note.png)Note:

If a macro has already been placed and a different variant of the macro is selected at the planning object, the placed macro can be updated via the Update detailed planning popup menu item. To do so select the Place macros again option in the [Update detailed planning](planninggui_d_detailplanungaktualisieren.htm) dialog.

Information row

In specific cases information about the assigned macro is displayed in the row below the Macro and Variant fields. This is for example done if an assigned macro was subsequently changed and the value sets in the planning object do not match those in the assigned macro:

- If a schematic page has already been created by means of the macro, you can update the data at the planning object via the button ![](../Pictures/Gui/ALL/all_update_as.png).
- If no schematic page has been generated yet, the data from the macro is automatically transferred to the planning object when the property dialog is opened for the first time.

The check run 028005 can be used to find different data at the planning object and macro.

![](../Pictures/Gui/ALL/info.png)Tips:

- In the pre-planning navigator use the popup menu item Update placeholder data to simultaneously update the data of placeholder objects at several planning objects. This popup menu item is also available in the segment template navigator in order to update the placeholder data at multiple segment templates simultaneously.
- If it should not be possible to edit a placeholder object in the pre-planning, deactivate the [Consider placeholder object in the pre-planning](macrosgui_r_platzhaltereinstellungen.htm#InVorplanungVerwenden) setting before creating the macro at the placeholder object. In this case the placeholder object is not displayed in this tab here after the macro has been assigned and can therefore also not be edited.

---

Properties group box

The table shows the placeholder objects and variables defined in the macro. The values of the variables can be selected via the value set selection or be edited manually.

If you select in the Value set row a value set, the entire column will be filled with values from this value set.

To edit, double-click a cell and, then, [...]. The Property selection dialog opens, and you can select a property of the planning object. In the Value column, the property number of the selected property is displayed instead of a specific value. Using block properties, you can also access properties of other objects that are linked to the planning object, e.g., properties of the part, the main function or PLC data.

When placing the macro, the values are determined once from the properties of the planning object or the linked objects, and carried over to the placed functions.

Popup menu:

The popup menu provides - depending on the field type (e.g. date, integer, multilingual) - the following menu items that are, depending on the situation, available for influencing the table or editing the values in the fields. You can find an overview of these popup menu items in the section [Popup menu items](userinterface_m_kontextmenu.htm).

See also

[Pre-planning](planninggui_k_start.htm)

[Placeholder objects: Structure and Operation](macrosgui_k_platzhalteraufbauarbeitsweise.htm)

[Assigning a Value Set to a Placeholder Object](macrosgui_h_wertesatzzuweisen.htm)

[Creating Detail Planning with Drag and Drop](planninggui_h_makrosdragdrop.htm)

[Block Properties](blockproperties_k_start.htm)