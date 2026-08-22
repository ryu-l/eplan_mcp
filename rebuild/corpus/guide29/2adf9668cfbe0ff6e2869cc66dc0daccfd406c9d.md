# Defining Terminal Strip Structure

![](../Pictures/Gui/ALL/note.png)Note:

This procedure is only supported by the program for compatibility reasons. We recommend that parts should be managed at the [main terminals](Glossary_o_hauptklemmen.htm).

However, a terminal strip structure by means of a device definition can only be defined if the terminal strip does not contain any main terminals or the property Do not use main terminals has been selected for the terminal strip.

Terminal strips exist in a variety of combinations of terminal types, quantities, and [accessories](Glossary_o_zubehoer.htm). Using a [device definition](devicelistgui_h_geraetedefinitionenanlegen.htm) (i.e. several [function templates](Glossary_o_funktionsschablonen.htm)) you can specify a custom terminal strip construction that cannot be subsequently changed in any way (e.g., by deletion of terminals). The function templates are saved in the terminal strip definition. The terminal strip construction can then only be deleted by deleting the individual function templates or the terminal strip definition.

For terminal strips, you can [create](Glossary_o_erstellen.htm) the device definition in the Edit terminal strip dialog by assigning function templates to the terminal strip definition. You create function templates from placed or unplaced terminals. Terminal [designations](Glossary_o_bezeichnungen.htm) can be assigned at that time but do not have to be.

The individual terminals are identified in the function template by the terminal designation, the function definition, and the level. If there is no terminal designation in the function template, the template works for any terminal designation in the project. If any terminal is deleted in the schematic, it will remain in the terminal strip and can be used or placed again.

The device definition (i.e., the terminal strip construction) can be transferred using the copy function or [macros](Glossary_o_makros.htm).

Preconditions:

- You have selected a terminal strip or terminal in the terminal strip navigator, the device navigator, or the graphical editor.
- The terminal strip only contains auxiliary terminals or the Do not use main terminals property has been activated for the terminal strip definition.

### Generate function templates

1. Select the menu item Project data > Terminal strips > Edit.
2. In the Edit terminal strip dialog select one or several terminals without assigned function templates. You recognize these by the icon in the Status column.
3. Select the Generate function templates popup menu item.  
     
   ![](../Pictures/Gui/ALL/arrow.png) For the corresponding terminals, the icon in the Status column changes.
4. Confirm your entries.

### Delete function templates

1. Select the menu item Project data > Terminal strips > Edit.
2. In the Edit terminal strip dialog select one or several terminals with assigned function templates. You recognize these by the icon in the Status column.
3. Select the Delete function templates popup menu item.  
     
   ![](../Pictures/Gui/ALL/arrow.png) For the corresponding terminals, the icon in the Status column changes.
4. Confirm your entries.

See also

[Dialog Edit terminal strip](stripmanagementgui_d_klemmenleistebearbeiten.htm)

[Using Main Terminals](terminalgui_k_hauptklemmen.htm)