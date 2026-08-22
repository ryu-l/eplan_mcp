# Dialog Import pre-planning data - <Project name>

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have opened a project, and have the pre-planning navigator open. Project data > Pre-planning > Import.

In this dialog, you can import lists with pre-planning data that were created in external applications.

Overview of the main dialog elements:

Type of data source:

Select the data source type from this drop-down list:

- Excel: Allows you to select an Excel file.
- Text: Allows you to select a text file as the data source.

Data source:

This field displays the file from which the pre-planning data are to be imported. Click [...] to select the data source in the dialog that opens in relation to the data type that you selected in the Type of data source field.

Target structure segment:

Here, you specify the hierarchy level in the tree view below which the imported data are to be inserted. The highlighted structure segment is pre-set. This drop-down list displays all the [structure segments](Glossary_o_struktursegmente.htm) defined in the project.

Field assignment:

This field displays the scheme that defines the assignment of the external data fields to the EPLAN [properties](Glossary_o_eigenschaften.htm). Click [...] to open the [Field assignment](planninggui_d_feldzuordnung.htm) dialog. There, you can [create](Glossary_o_erstellen.htm) or edit a scheme.

Ignore errors:

If this check box is enabled, the import will not be aborted because of errors and messages that occur.

If the check box is disabled, the import will be aborted as soon as an error occurs.

Overwrite existing planning objects:

If this check box is enabled, existing [planning objects](Glossary_o_planungsobjekte.htm) will be overwritten with the data from the planning [objects](Glossary_o_objekte.htm) of the same name from the import file.

If this check box is disabled, existing planning objects remain unchanged.

Do not generate any new structure segments and planning objects:

If this check box is enabled, only data of existing structure [segments](Glossary_o_segmente.htm) and planning objects will be updated. No new structure segments and planning objects are generated; the corresponding entries in the import file will be ignored.

If the check box is disabled, all data are imported from the import file, and, if necessary, new structure segments and planning objects are generated.

Delete missing objects in the project during re-import:

If this check box is activated, segments that are missing during a renewed import in the data source, i.e. were removed, are displayed in the subsequent dialog Synchronize pre-planning data and identified as deleted. These segments are deleted in the project unless the "None" action is set.

If the check box is deactivated, the segments that were removed in the data source are retained in the project.

See also

[Pre-planning](planninggui_k_start.htm)

[Import pre-planning data](planninggui_h_importvorplanung.htm)

[Dialog Synchronize pre-planning data](planninggui_d_importabgleich.htm)