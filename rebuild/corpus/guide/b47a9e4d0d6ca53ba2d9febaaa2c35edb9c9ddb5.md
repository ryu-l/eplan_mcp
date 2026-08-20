# Dialog Settings: General (projects, devices)

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have opened a project. File > Settings > Projects > "Project name" > Device > General.

In this dialog you define, on a project-specific level, general settings for devices, for example how devices are to be synchronized.

Overview of the main dialog elements:

Group box Synchronization

Empty properties overwrite filled properties:

When synchronizing functions that belong together, the properties of one function are adopted by the other functions. In general, the property values of the source function are copied into the properties of the target function. This check box applies to properties of source functions that contain no entries. If it is selected, then the target function adopts the empty entries. Existing entries in the target function are thus deleted. If the check box is deselected, then the target function does not adopt the empty entries. Existing entries are retained.

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

Check box is selected.

| Source function - without an entry | Target function before synchronization | Target function after synchronization |
| --- | --- | --- |
| Remark:\_\_\_\_\_\_ | Remark: DC | Remark: \_\_\_\_\_\_\_\_\_ |
| Remark:\_\_\_\_\_\_ | Remark: \_\_\_\_\_\_\_\_\_\_ | Remark: \_\_\_\_\_\_\_\_\_ |

Check box is deselected.

| Source function - without an entry | Target function before synchronization | Target function after synchronization |
| --- | --- | --- |
| Remark:\_\_\_\_\_\_ | Remark: DC | Remark: DC |
| Remark:\_\_\_\_\_\_ | Remark: \_\_\_\_\_\_\_\_\_\_ | Remark: \_\_\_\_\_\_\_\_\_ |

Filled properties overwrite empty properties:

This check box applies to properties of source functions that contain entries. If it is selected, then the target function without an entry adopts the source function entry. If it is not selected, then the target function without an entry does not adopt the source function entry. The target function remains without an entry.

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

Check box is selected.

| Source function - with entry | Target function before synchronization | Target function after synchronization |
| --- | --- | --- |
| Remark: Three-phase current | Remark: \_\_\_\_\_\_\_\_\_\_ | Remark: Three-phase current |
| Remark: Three-phase current | Remark: DC | Remark: Three-phase current |

Check box is deselected.

| Source function - with entry | Target function before synchronization | Target function after synchronization |
| --- | --- | --- |
| Remark: Three-phase current | Remark: \_\_\_\_\_\_\_\_\_\_ | Remark: \_\_\_\_\_\_\_\_\_ |
| Remark: Three-phase current | Remark: DC | Remark: Three-phase current |

---

Consider macro when generating devices:

This setting determines whether the functions from the macro entered at the part and not placed immediately are to be generated as unplaced functions during the generation of a new device in the navigators (via the New device and New terminals (devices) popup menu items) or in the graphical editor (via the menu item Insert center). The check box is deactivated by default.

The setting has the following effect in the Navigators:

| Check box | Result |
| selected | All functions from the macro are generated as unplaced functions if they belong to a device. If a function occurs twice in one of the macro variants, no further functions from the macro variant and from all the subsequent variants are taken into consideration. The behavior does not depend on whether the part contains function templates or not. |
| deselected | From the first main function which is entered in the function templates, an unplaced function is generated. The other templates remain free. If the part does not contain function templates, only the first main function from the macro is generated as an unplaced function. |

In the graphical editor, the setting has the following effect:

The part contains function templates and a macro file is stored with it. The functions matching the templates are distributed across several macro variants. When inserting devices from the Insert center, only the first macro variant (matching the page type) is, however, inserted.

| Check box | Result |
| --- | --- |
| selected | The functions from the further macro variants that belong to a device are generated as unplaced functions. If a function occurs twice in one of the macro variants, no further functions from the macro variant and from all the subsequent variants are taken into consideration. |
| deselected | The other templates for which no matching function in the first macro variant is found remain free. |

Add required accessories automatically:

If this check box is activated, required accessories are added automatically when inserting or generating devices. Required accessories are (individual) accessory parts for which the Required check box has been selected in parts management on the Accessories tab. Accessories from required accessory lists are only taken into consideration if the Insert complete accessory list property has been activated for the accessory list.

- If a device is inserted in the graphical editor via the Insert center, for example, not only the functions of the device are offered for placement but also the functions of the required accessory parts.
- When an unplaced device is, for example, generated in the device navigator via the New device popup menu item, the function templates for the required accessories are also added to the unplaced main function of the device.

After the device has been inserted or generated, the part numbers of the accessories are also entered in addition to the part number of the main function in the property dialog of the main function in the Part tab.

If the check box is deactivated, the device is inserted or generated without accessories. In this case the accessories must first be added via a device selection and then later placed from the device navigator.

Start device selection for selectable accessories:

If the Add required accessories automatically check box is activated, you can use it to specify whether the device selection is to be started automatically for selectable accessories.

Selectable accessories means that the part has at least one individual accessory part for which the Required check box is deactivated or that an accessory is an accessory list. Accessory lists generally allow you to select an accessory part from a list of possible alternatives. Required accessory lists for which the Insert complete accessory list property is activated are added completely directly without device selection.

If this check box is activated, the Device selection dialog is opened when devices are inserted or generated. The matching main part is already selected there. The associated accessory part(s) can be selected in the Accessories list by clicking in the Selection column and then clicking [...].

If the check box is deactivated, the device is only inserted with the required accessories, but without selectable accessories.

Output parts according to their position:

If this check box is activated, the parts and part reference data are output according to their position, regardless of whether there are empty lines between parts entries or not. However, the setting does not affect parts of the "Assignment Source / Target" type or terminal accessories.

If the check box is deactivated, parts are output regardless of their position.

See also

[Synchronizing Distributed Functions](adjustdata_h_funktionabgleichen.htm)

[Synchronization and Correction Run](adjustdata_k_start.htm)

[Procedure for Inserting Devices](devicelistgui_k_vorgehengeraeteeinfuegen.htm)

[Parts Management: Accessories Management](articlesgui_k_zubehoerlisten.htm)