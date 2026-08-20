# Modifying the Size of Mounting Surfaces

After importing STEP data, you can generate mounting surfaces on the imported 3D objects. If several 3D objects are combined into an item in the STEP data to be imported (e.g., mounting panel and support), it is possible that the mounting surface generated on it is geared to the dimensions of the attachments. Thus, the origin of the mounting surface is outside of the area set aside for the placement. The placing of devices is, thus, possible there as well, but not desired.

![](../Pictures/Visualisation/ALL/cabinetgui_moveorigin1_as.png)

To prevent errors in the placement of a device relative to the origin of the mounting surface, the size of the area set aside for the placement can be changed, and the position of the origin can thus be adjusted.

Preconditions:

- You have opened a project.
- You have opened the layout space navigator and a layout space.
- You have defined surfaces of an item as mounting surfaces.

1. Select a mounting surface of an item in the navigator.
2. Select the Mounting surface > Change size popup menu item in the navigator.  
     
   ![](../Pictures/Gui/ALL/arrow.png) Two vertical and two horizontal lines will appear that delimit the size of the mounting surface. The origin is always on the bottom left at the intersection of the left and bottom lines.
3. Click one after the other on the lines and move these.  
     
   ![](../Pictures/Gui/ALL/arrow.png) After the lines have been placed, the size of this mounting surface is redefined.  
     
   ![](../Pictures/Visualisation/ALL/cabinetgui_moveorigin2_as.png)  
     
   ![](../Pictures/Gui/ALL/arrow.png) The area set aside for the placement is redefined; the origin is set accordingly.  
     
   ![](../Pictures/Visualisation/ALL/cabinetgui_moveorigin3_as.png)

See also

[Defining a Mounting Surface](cabinetgui_h_montageflaechedefinieren.htm)

[Aligning the X-Axis / Y-Axis of Mounting Surfaces](cabinetgui_h_xyachseausrichten.htm)