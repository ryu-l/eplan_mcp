# Manually Assigning Cable Connections

You can manually change the assignment of cable connections to the connections of the cable part in the Edit cable dialog. This dialog displays the function templates existing in the cable part, the cable connections of the cable defined in the project, as well as their assignment. In order to display function templates in the Edit cables dialog, the selected cable must have a part assigned to it.

A placed or unplaced cable connection superimposes the function template (i.e., the connection of the cable part) if it has the same identifying properties. In this case, the name of the shield is taken into consideration first. If no suitable connection with shield is found for a function template with shield, this template is assigned a connection without shield (as long as the remaining identifying properties match). The shields thus do not necessarily have to be drawn into the schematic.

The assignment of the cable connections to function templates is done by moving and exchanging the connections in the table Connections of the dialog. The sequence of the function templates corresponds to the display in the tree view of the cable navigator and always remains the same.

![](../Pictures/Gui/ALL/info.png)Tip:

To open the Edit cable dialog, you can also select a cable definition line, a shield, or a connection definition point in the graphical editor and select the following commands: Tab Connections > Command group Cables > Edit.

### Assign free function templates to connections

Connections can only be moved to free function templates. Other connections are not changed when doing so.

PE / PEN and SH potential type connections cannot be moved to function templates with other potential types; nor can they be moved to another shield. Connections without shields, however, can be assigned to a function template with shielding.

1. Select the following commands: Tab Connections > Command group Cables > Navigator.
2. In the Cables - <Project name> dialog, select a cable definition, a (placed) cable connection, or a shield.
3. Select the Edit popup menu item.  
     
   ![](../Pictures/Gui/ALL/arrow.png) In the Edit cable dialog all connections of the associated cable as well as the function templates of the associated cable part are displayed.
4. In the Connections table select a connection and move it using the arrow buttons to the position where there is a free function template.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The connection accepts the data from the function template.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The data at the connection definition points are correspondingly updated. Existing data are overwritten. New data are only written to the connection definition points if these are not yet entered at the associated cable definition line / shield.

### Exchanging connections

Connections can only be exchanged if the potential type matches. PE /PEN and SH connections can be exchanged amongst themselves but not with other connections. Nor can connections in different shields be exchanged.

1. Select the following commands: Tab Connections > Command group Cables > Navigator.
2. In the Cables - <Project name> dialog, select a cable definition, a (placed) cable connection, or a shield.
3. Select the Edit popup menu item.  
     
   ![](../Pictures/Gui/ALL/arrow.png) In the Edit cable dialog all connections of the associated cable as well as the function templates of the associated cable part are displayed.
4. Select two connections in the Connections table and click ![](../Pictures/Gui/ALL/all_arrowswap_as.png) (Exchange).  
     
   ![](../Pictures/Gui/ALL/arrow.png) The rows are exchanged in the table.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The values of the Pair index, Color / number, and Cross-section / diameter properties are exchanged on the connection definition points.

![](../Pictures/Gui/ALL/note.png)Note:

If you exchange two shields in the Edit cable dialog, it has an indirect effect on the shielded cable connections. If the shield name of the shielded cable connections changes, they will no longer match their function templates. The changes resulting from this are displayed immediately.

See also

[Dialog Edit cable](cablegui_d_kabelbearbeiten.htm)