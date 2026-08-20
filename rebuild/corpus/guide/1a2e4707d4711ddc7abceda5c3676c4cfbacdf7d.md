# Generating Unplaced Connections

Unplaced connections are connections between connection points that you have not yet placed on a page. You can generate unplaced connections as connections between connection points. When generating the connections, you can generate the conductor / wire connections, use existing cables, or create new cables.

### Generate an unplaced conductor / wire connection

Precondition:

You have created at least 2 devices that have connection points.

1. Select the following commands: Tab Devices > Command group Devices > Navigator.
2. Select a device that has connection points and that is to be the connection source.
3. Select the following commands: Tab Devices > Command group Devices > Drop-down button Extras > Interconnect devices.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The Interconnect devices dialog opens.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The selected device is automatically displayed in the Device source field. The connection points of the selected device are displayed in the Connection point column.
4. Next to the Device target field, click [...], select the device that is to be the connection target in the subsequent dialog and then click [OK].  
     
   ![](../Pictures/Gui/ALL/arrow.png) The selected device is automatically displayed in the Device target field. The connection points of the selected device are displayed in the Connection point column.
5. Select the same number of connection points at the right and left of the dialog.  
     
   ![](../Pictures/Gui/ALL/arrow.png) If you have selected different numbers of connection points, the smaller number of connections are created. If you have selected more connection points than available cable connections, the connection points are connected using only the cable connections available.
6. To generate conductor / wire connections, click [Generate connections].  
     
   ![](../Pictures/Gui/ALL/arrow.png) The connections are generated.

### Generate unplaced cable connection

Precondition:

You have created at least 2 devices that have connection points.

1. Select the following commands: Tab Devices > Command group Devices > Navigator.
2. Select a device that has connection points and that is to be the connection source.
3. Select the following commands: Tab Devices > Command group Devices > Drop-down button Extras > Interconnect devices.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The Interconnect devices dialog opens.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The selected device is automatically displayed in the Device source field. The connection points of the selected device are displayed in the Connection point column.
4. Next to the Device target field, click [...], select the device that is to be the connection target in the subsequent dialog and then click [OK].  
     
   ![](../Pictures/Gui/ALL/arrow.png) The selected device is automatically displayed in the Device target field. The connection points of the selected device are displayed in the Connection point column.
5. Select the same number of connection points at the right and left of the dialog.  
     
   ![](../Pictures/Gui/ALL/arrow.png) If you have selected different numbers of connection points, the smaller number of connections are created. If you have selected more connection points than available cable connections, the connection points are connected using only the cable connections available.
6. To use the connection of an existing cable, next to the Cable DT field, click [...], select a cable from the subsequent dialog and then click [OK].
7. To use the connection of an new cable, next to the Cable type field, click [...], select a suitable part from the subsequent dialog for the cable type and then click [OK].
8. Enter a DT for the cable in the Cable type field.
9. To directly open the cable in the Edit cable dialog after the connection has been generated, select the Edit cable check box.
10. Click [Generate connections].  
      
    ![](../Pictures/Gui/ALL/arrow.png) The connections are generated.  
      
    ![](../Pictures/Gui/ALL/arrow.png) The cable is automatically displayed in the Edit cable dialog.  
      
    ![](../Pictures/Gui/ALL/arrow.png) If you have created a cable, the new cable is displayed in the cable navigator (Tab Connections > Command group Cables > Navigator).

See also

[Placing Connected Functions](planningconnections_h_platzieren.htm)

[Connection Pre-planning](planningconnections_k_start.htm)

[Unplaced Connections](connectionbrowsergui_k_npv.htm)

[Automatically Generating Functions Using a Numbering Pattern](navigatorgui_h_mehrerfunktionerzeugen.htm)