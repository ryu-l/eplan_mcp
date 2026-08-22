# Dialog Select macro

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have opened a project. You have opened a project page in the graphical editor. There are [macros](Glossary_o_makros.htm) of the desired type available.

- Insert > Window macro / symbol macro
- Page > Page macro > Insert

In this dialog, you can select the desired macro. Note that a multiple selection is possible for page macros!

Overview of the main dialog elements:

Preview:

Select this check box in order to display, on the right side of the dialog, the graphical preview of the macro selected in the list on the left side of the dialog. When inserting [page macros](Glossary_o_seitenmakros.htm) you can display up to 12 pages in the preview.

Below the graphical preview is a comment field that cannot be edited. The following specifications are made in rows for a macro selected in this field:

- Version: only for macros from [macro projects](Glossary_o_makroprojekte.htm)
- Source project: the project from which the macro originates
- Description: The text stored as the description when creating macros (can be more than one line); or the property Macro: Description ([ID](Glossary_o_id.htm) 11057) if an automatically generated page macro is selected. If different descriptions are stored in a page macro, only the description of the first page of the page macro is displayed.
- Source / Reference: only for [window macros](Glossary_o_fenstermakros.htm) created from [DXF](Glossary_o_dxf.htm) / [DWG](Glossary_o_dwg.htm) files. "DXF" stands for macros from DXF files and "DWG" for macros from DWG files.
- Number of pages: only for page macro.

File type:

This field displays the selected macro type. When inserting window or [symbol macros](Glossary_o_symbolmakros.htm), both of the file types "Window macro (\*.ema)" and "Symbol macro (\*.ems)" and also the entry "Window macro, Symbol macro (\*.ema, \*.ems)" are available. If you insert page macros you can access all macro types in the drop-down list. This allows you to insert window and symbol macros as new pages as well.

Representation type:

Not available for page macros! The representation type of the macro is used for sorting, i.e., it helps you manage your macros. It has no effect on the [functions](Glossary_o_funktionen.htm) within the macro, these retain their own respective [representation types](Glossary_o_darstellungsarten.htm). This allows all macros belonging to a [part](Glossary_o_artikel.htm) to be stored in a single file. Up to 26 representation type [variants](Glossary_o_varianten.htm) are possible for a single macro. The representation type is set to default values according to the selected functions or the page type. Select the desired entry from the drop-down list:

- Multi-line: For macros placed on multi-line schematic pages.
- Multi-line Fluid: For macros placed on multi-line Fluid power schematic pages.
- Overview: For macros placed on overview pages.
- Pair cross-reference: For macros used to implement a pair cross-reference.
- Single-line: For macros placed on single-line schematic pages.
- P&I diagram: For macros placed on [P&I diagram](Glossary_o_ri_fliessbild.htm) pages.
- Graphic: For macros containing only graphical components. Graphical components are not included in [reports](Glossary_o_auswertungen.htm), [check runs](Glossary_o_prueflaeufe.htm), or the creation of [cross-references](Glossary_o_querverweise.htm) and are also not acquired as targets.
- Part placement: For macros placed on [mounting panels](Glossary_o_montageplatten.htm).

![](../Pictures/Gui/ALL/note.png)Note:

If a function has several representation types, whose common [properties](Glossary_o_eigenschaften.htm) contain varying data, the representation type will determine which properties will be considered during reporting. EPLAN uses the specified [sequence of the representation types for its global editing and reporting](reverseengineering_k_reihenfolge.htm).

Variant:

Not available for page macros! If you have created multiple variants from one macro, you can use this drop-down list to select the desired variant. The selected variant is also displayed in the preview.

Path:

The path (including the drive) selected in the Look in field is displayed here. The path can be set to the macro directory specified in the [settings](Glossary_o_einstellungen.htm) by using the Go to default popup menu item.

See also

[Inserting Macros](macrosgui_h_makrosauswaehlen.htm)