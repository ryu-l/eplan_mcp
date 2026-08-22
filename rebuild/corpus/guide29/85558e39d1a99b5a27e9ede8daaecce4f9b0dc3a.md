# Generating Drilling Patterns from NC Files

The import of drilling information from Rittal - Perforex / Secarex NC files encompasses the files with the following file extensions:

- Items \*.PBT
- Variable [items](Glossary_o_bauteile.htm) \*.PVB
- Outlines \*.PKU.

![](../Pictures/Gui/ALL/note.png)Notes:

- With this method only [drilling patterns](Glossary_o_bohrbilder.htm) for individual items can be generated, not however complete [mounting panels](Glossary_o_montageplatten.htm) from Rittal - Perforex / Secarex item files (\*.PBT or \*.PVB).
- A [user-defined](Glossary_o_benutzerdefiniert.htm) outline is created from a Rittal - Perforex / Secarex outline file (\*.PKU). An "NC Rittal - Perforex / Secarex" record is already assigned to this outline. After the import you [create](Glossary_o_erstellen.htm) a drilling pattern with drill type "User-defined outline" that uses the outline created by the import of the PKU file in the parts management.
- An outline created from a Rittal - Perforex / Secarex outline file should be checked in the outline editor before a drilling pattern is created. For example, whether the outline is closed, the position of the pilot drill hole at rectangular milling cuts, whether the NC record is correct, the number of rounding elements at milled roundings.
- Outline files from user-defined [outlines](Glossary_o_konturen.htm) of the NC Rittal - Perforex / Secarex import often correspond to the standard drill types (rectangular, oblong, hexagonal, octagonal). In order to simplify the drilling pattern to be created such user-defined outlines can also be replaced by the corresponding drill types for which, furthermore, no additional NC record is required.
- An automatic [NC record](ncgui_k_ncdatensatz.htm) cannot be generated for round milling outlines while importing a PKU file since the starting point for an NC record can only be defined on straight outline [segments](Glossary_o_segmente.htm) in .EPLAN Pro Panel. Round [cut-outs](Glossary_o_durchbrueche.htm) from PKU files should therefore be defined as [drill holes](Glossary_o_bohrungen.htm) or as threaded holes in the parts database.

Preconditions:

- You have opened a project.
- You have created NC files with the file extension PBT, PVB and PKU using the Rittal - Perforex / Secarex software.

1. Select the menu items Utilities > Generate drilling patterns / outlines > From Rittal - Perforex / Secarex NC files.
2. In the file selection dialog select the Rittal - Perforex / Secarex NC files to be imported and click [Open].
3. If you have selected a PKU file for importing, select the directory in which the outlines are to be created from the NC files in the dialog Generate drilling patterns / outlines. The default directory is the directory for [macros](Glossary_o_makros.htm).
4. Select a scheme for the Rittal - Perforex / Secarex NC machine that is to be used when exporting the Rittal - Perforex / Secarex NC data. The drill type and diameter for the drill holes in the drilling patterns are determined from these [settings](Glossary_o_einstellungen.htm).
5. Click [OK].  
     
   ![](../Pictures/Gui/ALL/arrow.png) A drilling pattern is generated in the parts database from a PBT or PVB file.  
     
   ![](../Pictures/Gui/ALL/arrow.png) A user-defined outline is generated in the macro directory from a PKU file.
6. In the parts database [generate](Glossary_o_erzeugen.htm) a new drilling pattern with a drill type "User-defined outline" and store the outline generated through importing the PKU file in it.

See also

[Tab Drilling pattern](partsmanagementgui_r_konstruktion.htm)

[Tab Cut-outs](partsmanagementgui_r_bohrbild.htm)

[Dialog Generate drilling patterns / outlines](cabinetgui_d_bohrbilderzeugen.htm)