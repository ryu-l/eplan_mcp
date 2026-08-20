# Locked Data in Multi-user Operation

If any property of an object is changed, all properties are locked. "Locking" always means a change lock, reading of the properties is still allowed for other users. After editing, the object is immediately unlocked again.

### Editing of pages and layout spaces

Only when a page or a layout space or an object is edited on a page or in a layout space, are the page or the layout space itself and all the functions that are placed on the same page locked for a second user.

If a user in multi-user operation is the second user to open a page or a layout space that has already been opened by another user, nothing happens. If a user edits, for example, the properties of a page or a layout space, a second user can also open the page or the layout space. Only if the second user, for example, wants to edit the properties of a device or also the page / layout space properties, will Eplan open the dialog [Multi-user conflict](xesmultiuserconflictgui_d_konflikte.htm).

### Editing of functions in the navigators

If you change a function in a navigator, it is locked during editing. When the function is placed, the page with all objects contained on it is locked in addition to the function. The superior and subordinate nodes of the function in the tree view are not locked unless the corresponding functions are placed on the same page as the changed function.

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

This allows a user to rename a terminal strip definition X1 placed on page 8 in the device navigator to X5, while another user edits an individual terminal of this terminal strip placed on page 6. In such a case only the terminal strip definition and not all functions of the terminal strip are renamed!

If, on the other hand, the entire terminal strip is to be renamed, the cursor must be positioned on the tree node that represents the device X1. Subsequently the user selects the menu item Rename in the popup menu and enters the new DT X5. During the process all functions with this DT are locked for another user.

See also

[Multi-user Operation](xesmultiuserconflictgui_k_start.htm)