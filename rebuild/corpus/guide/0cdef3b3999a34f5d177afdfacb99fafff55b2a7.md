# Dialog Assign pages

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have opened a project. File > Import > Command group Project data > Project data > Command group Page > DXF / DWG. In the DXF / DWG file selection dialog, choose (at least) one file and click [Open]. You may have to change the import settings in the DXF / DWG import dialog and start the import by clicking [OK].

In this dialog you specify how new project pages are to be handled.

Overview of the main dialog elements:

Target:

The data fields available for the import target depends on the page structure of the target project. The following columns are available:

- Overwrite: Select this check box to specify whether an existing page should be overwritten or not when importing a DXF / DWG file.
- Function designation / location designation ...: In the fields for function designation, location designation, etc., click [...], to select a different function designation / location designation from the list of existing options in the current project.
- Page name: In this field you can manually overwrite the default setting.
- Suppl. field: Sheet no.: The sheet number is a supplementary property of page names. If necessary, define any extra information for the imported page here.

Popup menu:

The popup menu provides - depending on the field type (e.g. date, integer, multilingual) - the following menu items that are, depending on the situation, available for influencing the table or editing the values in the fields. You can find an overview of these popup menu items in the section [Popup menu items](userinterface_m_kontextmenu.htm).

[Number]:

Opens the [Number pages](pagebrowsergui_d_seitennummerierung.htm) dialog, where you can automatically assign page names.

![](../Pictures/Gui/ALL/note.png)Note:

If you have selected the Scaling dialog option in the Import tab in the settings (File > Settings > User > Interfaces > DXF / DWG export and import), the dialog Import formatting is opened before the actual import procedure and you can edit the automatically determined drawing limits.

See also

[Dialog Import formatting](xdxfgui_d_importformatierung.htm)