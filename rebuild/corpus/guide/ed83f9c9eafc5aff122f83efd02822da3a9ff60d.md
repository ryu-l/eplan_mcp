# Tab General (wire fabrication)

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

- File > Settings > Company > Wire fabrication > "Machine" > Tab General
- File > Export > Command group Manufacturing data > Wire fabrication > "Machine". Click [...] next to the Scheme field. Select the General tab.

In this tab, you specify the file path and file name for the export of wire data to the following wire fabrication machines.

- Rittal - WireTerminal WT
- Steinhauer - PWA
- CadCabel
- Metzner - Triathlon
- Schleuniger - Easy ProductionServer

In addition the settings also apply for the export of the general wires parts list.

Overview of the main dialog elements:

File path:

Select the directory where the export files are to be saved. Click ![](../Pictures/Gui/ALL/all_selectdirectory_as.png) to open the Select folder dialog and then navigate to the desired directory, or create a new one. You can use the Insert path variable popup menu item to branch to the dialog [Select path variable](modaldialogsdb_d_pfadvariablen.htm) where you can select one of the available path variables.

File name:

Here, you can enter the name of the file to be generated or select it by using ![](../Pictures/Gui/ALL/all_selectfile_as.png) in the Save as dialog. The file name extension is derived from the machine format selected. If through the export several files are to be generated with different file name extensions, the name entered here will apply to all files.

Some file names and / or file name extensions are set by the manufacturer. In such a case, you can set only the file path.

Character set (only "General wires parts list" format):

This setting allows you to extend the character set of the text file to be created so that, for example, connection point designations can also be output with special characters or in Eastern European or Asian languages. The following formats are available in the drop-down list:

- ANSI: The characters are stored using the ANSI code. Use this coding when you want to edit the generated bill of materials file in Windows applications.
- ASCII: The characters are stored using the ASCII code. Use this coding when you want to edit the generated bill of materials file in MS-DOS applications.
- UNICODE: The characters are stored using Unicode. The bill of materials file is then independent of the platform and operating system.

![](../Pictures/Gui/ALL/note.png)Note:

Before an extended character set is used for the export of the general wires parts list, you should check whether the target processing programs of the machines and printers can handle this character set. If problems arise, you should use the default setting "ANSI".