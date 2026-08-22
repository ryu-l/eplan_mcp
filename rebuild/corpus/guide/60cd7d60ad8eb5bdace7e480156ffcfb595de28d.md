# Dialog Export records

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

Tab Master data > Command group Parts > Management. In the Parts management dialog you have opened a parts database using [Extras] > Settings.

- Button [Extras] > Export.
- You have selected the records to be exported in the tree or in the list. Select the Export popup menu item.

In this dialog, you can specify the export settings.

Overview of the main dialog elements:

File type:

Select the desired file type from the drop-down list. Possible settings are "Eplan Data Portal exchange format (EDZ)" and "XML".

Click [...] to specify how the data are to be exported for the Eplan Data Portal exchange format (EDZ): Activate the check box Export referenced data completely if subassemblies, submodules, etc. are to be included in the export in the case of assemblies, modules, etc.

Entire file:

Select this option if you want to export the selected data in one file. In this case, the File name field is enabled; here, enter the name for the export file or click ![](../Pictures/Gui/ALL/all_selectfile_as.png) to select it interactively. The file name extension is automatically appended to match the file type selected in the File type field, (for example .xml for the "XML" file type).

You can use the Insert path variable popup menu item to branch to the dialog [Select path variable](modaldialogsdb_d_pfadvariablen.htm) where you can select one of the available path variables.

Individual files:

Select this option if you want to export the selected data as single files. In this case, the Directory field is validated, and it is here that you specify the directory to which the data to be exported will be output as files. The file name of the respective export file corresponds to the part number, the name of the drilling pattern, the name of the manufacturer, etc.

Record type:

This setting is only available if you export the entire parts database or a subset, meaning that you have opened the dialog via [Extras] > Export. Use the check boxes in this section to select the data to be exported.

By using the record type "Property" you can export the user-defined properties for the parts that were created in the [Configure properties](eservicesgui_d_konfigeigenschaften.htm) dialog.

Trade:

This setting is only available if you export the entire parts database or a subset, meaning that you have opened the dialog via [Extras] > Export. Use the check boxes in this section to select which trades should be exported; if a trade is selected, then all part types belonging to that trade will be exported. For the Fluid area, you can further limit or extend the scope for the export.

See also

[Exporting Parts Data](articlesgui_h_artikelexportieren.htm)