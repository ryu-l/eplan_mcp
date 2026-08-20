# Defining Drilling Patterns Graphically

Drilling patterns can also be defined graphically in a macro project, without using data from imported NC or DXF / DWG files. The process encompasses four working steps:

- Drawing of the outline of the item and of the required drill holes on a graphics page
- Assigning the identifying layers for the drilling pattern generation
- Inserting a drilling pattern frame
- Automatic generation of the drilling pattern.

Precondition:

You have opened a macro project.

1. Open a graphics page on a 1:1 scale.
2. Draw the outline of the item and the drill holes required in it true to scale.
3. Open the properties dialog of the each element and bring the Format tab to the front. Change the layers of the elements specified for the drilling pattern as shown in the following table in the Layer property below the Format hierarchy level.

| Element | Name (layer), description | |
| --- | --- | --- |
| Outline item | EPLAN802, Graphic.Drilling pattern generation.Items | |
| Drill holes (all drill types) | EPLAN803, Graphic.Drilling pattern generation. Drill holes | |
| Threaded holes | EPLAN804, Graphic.Drilling pattern generation. Threaded holes | |
| User-defined outlines | EPLAN805, Graphic.Drilling pattern generation.Outlines | |

4. Insert a drilling pattern frame that encompasses the elements intended for the drilling pattern. Select the following commands: Tab Master data > Command group Drilling pattern frame > Insert.  
     
   ![](../Pictures/Gui/ALL/arrow.png) A point of origin is set at the bottom left at the outline of the item.
5. Enter the name, a description and a directory for the user-defined outlines to be created in the properties dialog of the drilling pattern frame.
6. Create the drilling patterns. Select the following commands: Tab Master data > Command group Drilling pattern / outline > Drop-down button Generate > From macro project (automatically).
7. Select whether the process is to be applied to the complete project or only to the selected drilling pattern frame.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The drilling patterns are shown in a top view in the parts management from the drawn objects that are assigned to the drilling pattern frames.

See also

[Inserting Drilling Pattern Frames](propanelmasterdata_h_bohrbildkasteneinfuegen.htm)