# Exporting Assignment Lists

The export of assignment lists is always CPU-related. The affiliation of a PLC card to a CPU is specified via the [CPU name](devicetaggui_r_spsstruktur.htm#CPU). A CPU is uniquely identified by specification of the CPU name in the form [Configuration project].[Station ID].[CPU identifier].

![](../Pictures/Gui/ALL/note.png)Note:

You can export only one separate list each for each processor (CPU). Therefore set the filter in the dialog Addresses / assignment lists so that the PLC addresses of only one CPU are displayed. The scheme that specifies the format of the PLC addresses is determined on the basis of the CPU that is contained in the selection and cannot be changed here. If no scheme is assigned to the CPU, the scheme specified in the project settings is used.

1. Select the following commands: Tab Devices > Command group PLC > Assignment list > Button [Extras] > Export assignment list (entire CPU).  
     
   ![](../Pictures/Gui/ALL/arrow.png) The scheme that specifies the format of the PLC addresses is displayed in the PLC-specific settings field in the dialog [Export assignment list (entire CPU)](plcgui_d_exportzuli.htm). The configuration project and the workstation name to which the CPU is assigned are further displayed via the field.
2. In the Language field, select a suitable language for the assignment list.
3. In the File name field, enter the name of the file where the exported data is to be stored.
4. Click [OK].  
     
   ![](../Pictures/Gui/ALL/arrow.png) The addresses from the assignment list are written to the export file. In the process all PLC cards with the same CPU name are considered.

![](../Pictures/Gui/ALL/info.png)Tips:

- Using the Create filter for CPU popup menu item in the table you can automatically generate a filter for the display of the PLC addresses based on the data of the highlighted row. The values of the Configuration project (indirect), PLC station: ID (indirect), and CPU (indirect) properties are used as filter criteria here.
- You can also access the Export assignment list (entire CPU) dialog via the Backstage view: File > Export > Command group Project data > Project data > Command group PLC > Assignment list > Button [Extras] > Export assignment list (entire CPU).

See also

[Dialog Settings: PLC](plcgui_d_allgemeinespseinstellungen.htm)

[Importing or Synchronizing Assignment Lists](plcgui_h_importzuli.htm)