# Importing Bills of Materials

You can import the parts data of a bill of materials into the current project. Please note that export and import can only be carried out within the same project.

Precondition:

You have opened a project.

1. Select the following commands: Tab Devices > Command group Devices > Bill of materials.
2. In the Bill of materials - <Project name> dialog, select the Import popup menu item.
3. In the Import bill of materials dialog select the drive and directory where the file to be imported is located. (To return to the default setting for a directory, click the Eplan icon in the left-hand navigation area and the directory listed below it.)
4. Select one of the entries for the format of the file to be imported from the file type drop-down list.
5. Select the desired import file from the list.
6. Click [Open].  
     
   ![](../Pictures/Gui/ALL/arrow.png) The records are imported. If errors occur during the import, a corresponding message is displayed. The details can be viewed in the message management (Tab Tools > Command group Review > Messages).

If you have exported and edited data, only certain fields from the export file are written back on import. An overview of the fields is provided in the section "[Bills of Materials: Export File Fields](partslistgui_k_felderexportdatei.htm)".

![](../Pictures/Gui/ALL/note.png)Note:

If a part reference is imported that is already assigned to a DT, the DT must already exist. Otherwise, a part reference for a Project part will be created.