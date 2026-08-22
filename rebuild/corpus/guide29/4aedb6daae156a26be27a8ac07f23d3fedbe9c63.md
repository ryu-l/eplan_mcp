# Dialog Export Copper DXF

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have opened a project. You have selected in the [layout space](Glossary_o_bauraum.htm) or layout space navigator copper [items](Glossary_o_bauteile.htm) for which an NC export is to be carried out. Utilities > Manufacturing data > Machining > Copper DXF.

Use this dialog to specify the [settings](Glossary_o_einstellungen.htm) for the graphical export of the [unfold](Glossary_o_abwicklung.htm) of copper items in the [DXF](Glossary_o_dxf.htm) format. The following data is transferred:

- External dimensions of the copper rail in the unfolded state, represented as a rectangle (width x unfolded total length)
- Bending [lines](Glossary_o_leitungen.htm)
- Bending extents
- Bending notes
- All mechanical [cut-outs](Glossary_o_durchbrueche.htm).

Overview of the main dialog elements:

Machine:

The delivery scope includes the machine definition named "Default". If you have defined other [schemes](Glossary_o_schemata.htm) in the company settings, you can select other machine definitions from the drop-down list.

The [...] button opens the Settings: Copper export DXF dialog where you can modify the settings for the scheme or define a new scheme.

Output directory:

This field displays the storage location. Here, the directory is pre-selected that is specified under Settings > Company > Machining for the copper export DXF.

You can use the Insert path variable popup menu item to branch to the dialog [Select path variable](modaldialogsdb_d_pfadvariablen.htm) where you can select one of the available [path variables](Glossary_o_pfadvariablen.htm).

Target file:

This field is active only if the selection contains copper items for which an unfold exists. Here, you can enter the name of the DXF file to be generated, or use [...] in the Open dialog to select a file of the Copper DXF (\*.dxf) file type. If this results in several files, the field is deactivated, and the conditions apply that are defined in the scheme for generating the file name and the subdirectories.

Apply to entire project:

If this check box is activated, the current selection will be extended to all unfolded copper items of the project.

If the check box is deactivated, only unfolds of highlighted items will be exported.

If you have already selected a single project (and not set any [filters](Glossary_o_filter.htm)), then this check box is automatically activated and grayed-out. You can then no longer change this setting.

See also

[Dialog Settings: Copper export DXF](ncgui_d_einstellungenncexportperdxf.htm)