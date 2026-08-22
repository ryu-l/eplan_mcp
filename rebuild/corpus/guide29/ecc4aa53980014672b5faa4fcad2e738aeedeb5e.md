# Defining Mounting Lines

Mounting [lines](Glossary_o_leitungen.htm) allow the placement of 3D [objects](Glossary_o_objekte.htm) on non length-variable [items](Glossary_o_bauteile.htm), for example C horizontal rails, similarly to on [mounting rails](Glossary_o_tragschienen.htm). Mounting lines have a definable alignment. This means that mounting lines can also be used to place 3D objects on sloping surfaces and in non-orthogonal mounting positions.

Mounting lines adopt the [Z direction](cabinetgui_h_anschlussdefinieren.htm#ZRichtung) of a surface selected during the definition. The Z direction indicates how the object to be placed on the mounting line is to be oriented.

Preconditions:

- You have opened a project.
- The [layout space](Glossary_o_bauraum.htm) navigator is open and a layout space is open.
- The layout space contains 3D objects.
- You have activated the object snap.

1. Select the Edit > Device logic > Mounting line menu items.
2. Move the cursor over the 3D objects.  
     
   ![](../Pictures/Gui/ALL/arrow.png) Points, edges or surfaces below the cursor are automatically highlighted. Snap points are displayed.
3. Select a surface whose Z axis determines the alignment of the mounting line.
4. Enter the starting point and the end point of the mounting line on the desired surface or edge.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The alignment of the mounting line is displayed with a coordinate cross.  
     
   ![](../Pictures/Visualisation/ALL/cabinetgui_mountingline1_as.png)
5. Enter the corresponding values in the fields Name and Description of the [property dialog](Glossary_o_eigenschaftendialog.htm).
6. Click [OK].  
     
   ![](../Pictures/Gui/ALL/arrow.png) 3D objects such as [cable](Glossary_o_kabel.htm) clamps can be placed on the entire length of the mounting line in the selected alignment.  
     
   ![](../Pictures/Visualisation/ALL/cabinetgui_mountingline2_as.png)

![](../Pictures/Gui/ALL/note.png)Tips:

- To subsequently change the alignment and rotation of a mounting line, use the [Rotate around axis](cabinetgui_h_drehenxyz.htm) functionality.
- Mounting lines can be moved in [macro projects](Glossary_o_makroprojekte.htm) like graphical elements by using Edit > Move or via Drag & Drop.

See also

[Displaying Mounting Aids](cabinetgui_h_montagehilfenanzeigen.htm)