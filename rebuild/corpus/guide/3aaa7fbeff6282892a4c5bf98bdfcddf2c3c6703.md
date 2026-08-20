# Dialog Page structure

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

- You have opened a project. Tab Home > Command group Page > Navigator. Select a project. Select the commands File > Information > Command group Project properties > Structure. Click [...] next to the Pages field.
- You have opened a project. Tab Home > Command group Page > Navigator. Select a project. Select the Properties popup menu item. Select the Structure tab. Click [...] next to the Pages field.
- You have selected a project management database. You have loaded directories and projects. File > Project management. Select a project. Select the Structure tab. Click [...] next to the Pages field.

In this dialog you can create, edit, and manage identifier schemes for identifying and numbering pages.

Overview of the main dialog elements:

Scheme:

This field contains the name of the current identifier scheme.

Select the scheme that you wish to use or edit from the drop-down list. You can also use the adjacent [toolbar](schemeconfig_m_schemaschaltflaechen.htm) for this purpose.

Object identifier:

The object identifier is required to structure pages according to the DIN EN 61355-1 standard. In doing so, the object identifier assigns a document (i.e. a project page) to a certain object (e.g. a function, a location, or a product).

![](../Pictures/Gui/ALL/note.png)Notes:

- To use the object identifier for structuring, the extended reference identification must have been activated in the project properties (Extended reference identification check box in the Structure tab).
- The object identifier may only be used in combination with the Document type identifier block. A combination of object identifier and other identifier blocks is not possible. If you activate the Use for structuring check box for using the object identifier, the table with the identifier blocks is therefore also grayed out (with the exception of the document type), und and the identifier sequence cannot be changed.

If the Use for structuring check box is activated, the object identifier is used to structure the project. The behavior with regard to the entry and reporting of the page structure is then changed as described in "[Identification of Pages in Accordance with DIN EN 61355-1](projectstructure_k_objektkennzeichen.htm)".

If the check box is deactivated, the behavior for entry and evaluation of the page structure corresponds to the behavior in previous Eplan versions (version 2.3 or older). In this case, the object identifier is not available as structuring element.

Table:

In the table you specify which identifier blocks are identifying, describing or not available for the page structure.

The identifier blocks are displayed in the tree view of the page navigator, in the page properties, etc. in accordance with the order specified in the table. You can change the identifier order of the identifier blocks by using the arrow buttons.

- Structure: Lists the identifier blocks which correspond to the page structure. The adjacent column displays the associated preceding signs.
- Value: In this column you use the drop-down list to specify whether the identifier block is identifying, describing or not available.

See also

[Project Structure: Basics](projectstructure_k_hinterg.htm)

[Editing Project Properties (Project Management)](prjmanagementgui_h_projekteigenschaftenloeschen.htm)

[Defining a User-defined Project Structure](projectstructure_h_frhierarchienerstellen.htm)

[Creating / Selecting a Project Management Database](prjmanagementgui_h_projekteverwalten.htm)