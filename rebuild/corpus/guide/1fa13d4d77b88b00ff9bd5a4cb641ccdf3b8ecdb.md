# Dialog Export PLC data

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have opened a project. File > Export > Command group Project data > Project data > Command group PLC > PLC data.

In this dialog, you export all PLC data in the project (i.e., the data of all valid PLC boxes and connection points) to an XML file. You can then (e.g.) exchange this data with various PLC configuration programs.

Data from various placements of a single function are combined together and are then redistributed to their original placements on import. For PLC boxes, only the data of the main function is exported.

Free function templates are not exported. I/O entries from assignment lists are also not exported.

Overview of the main dialog elements:

Configuration projects:

All configuration projects are displayed in the drop-down list. Select the desired project. The export considers all cards with their connection points which contain the corresponding value either at the PLC box in the field Configuration project or at one of their network / bus cable connection points in the property Configuration project (at PLC boxes and bus ports).

Language:

All languages defined in the translation settings for the project are displayed in the drop-down list. Select the language in which the PLC data is to be exported. The data is always single-language.

At [PLC Data Exchange in AutomationML AR APC Format](plcgui_k_amlbusdatenaustausch.htm) all languages are exported. The language set here is the main language in the exchange file.

PLC configuration program:

This drop-down list displays all available combinations of manufacturers and PLC configuration programs. Select the desired entry.

Format of export file:

The supported formats of the PLC configuration program that is selected in the field are displayed in the drop-down list. Select the desired format.

File name / file path:

In this field, you enter the name of the file used to save the export file. Click ![](../Pictures/Gui/ALL/all_selectfile_as.png) to open the file selection dialog and change to any desired directory.

You can use the Insert path variable popup menu item to branch to the dialog [Select path variable](modaldialogsdb_d_pfadvariablen.htm) where you can select one of the available path variables.

If you have selected the "Siemens SIMATIC STEP 7 5.6" entry in the PLC configuration program field, enter a file path here and not a file name. Click [...] to open the Select directory dialog for selecting a directory. On export, a file is generated per station in the specified directory, with the station ID as the file name. (A configuration project can contain several stations, whereby you specify the station ID as a property of the PLC box.) If a file of the same name already exists in the specified directory, then a query is displayed asking if you wish to overwrite the file.

[Options]:

This button is active when an AutomationML AR APC format has been selected in the Format of export file field. In the [subsequent dialog](plcgui_d_optionsaml.htm) you specify the degree of detailing for the export file.

See also

[Dialog Import PLC data](plcgui_d_importbuskonfig.htm)