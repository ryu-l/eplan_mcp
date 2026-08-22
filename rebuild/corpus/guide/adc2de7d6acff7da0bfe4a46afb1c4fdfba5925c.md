# Dialog Export drilling template

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have opened a project. In the layout space or in the layout space navigator, you have selected objects for which you want to execute an NC export. File > Export > Command group Manufacturing data > Machining > Drilling template.

Use this dialog to specify the settings for the export of manufacturing data for machining. A file in the format "PDF" is exported with the geometric positions / coordinates of

- Drill holes
- Threads
- Outlines.

The PDF file is printed on paper and placed on the item as a template. Machining is carried out mechanically by drilling / milling at the marked positions.

Overview of the main dialog elements:

Machine:

The delivery scope includes the machine definition named "Default". If you have defined other schemes in the company settings, you can select other machine definitions from the drop-down list.

The [...] button opens the Settings: Export drilling template dialog where you can modify the settings for the scheme or define a new scheme.

Output directory:

This field displays the storage location. The directory that is defined for the drilling templates export in the company settings is pre-selected here.

You can use the Insert path variable popup menu item to branch to the dialog [Select path variable](modaldialogsdb_d_pfadvariablen.htm) where you can select one of the available path variables.

Target file:

This field is active only if the selection contains objects that can be exported (e.g., a mounting panel). Here, you can enter the name of the PDF file to be generated or select it via ![](../Pictures/Gui/ALL/all_selectfile_as.png) in the Save as dialog. If this results in several files, the field is deactivated, and the conditions apply that are defined in the scheme for generating the file name and the subdirectories.

See also

[Dialog Settings: Export drilling template](ncgui_d_einstellungenncbohrschablone.htm)