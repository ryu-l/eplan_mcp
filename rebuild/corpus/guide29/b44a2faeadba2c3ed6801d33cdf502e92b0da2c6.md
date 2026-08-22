# Data of the Generated Macros

Macros created or automatically generated in EPLAN contain the following data:

- Macro name
- Version
- Source project
- Description
- Source / reference.

In the "Source project" property, EPLAN enters the project where the macro was originally created. The "Version" and "Source / reference" can only be edited in a macro project. These fields remain empty for [macros](Glossary_o_makros.htm) created in a standard manner in a schematic project. When inserting macros this data is displayed for you in a comment field.

All macros also have page data. This allows you to insert a window or symbol macro as a page macro. If this macro is inserted as a cut-out of an existing page, the "page" in the macro is ignored.

Function definitions, [symbols](Glossary_o_symbole.htm), parts, [forms](Glossary_o_formulare.htm) and [plot frames](Glossary_o_normblaetter.htm) are not stored in macros. Only sources and numbers / names are saved in macros.

If you insert a macro and one of the [objects](Glossary_o_objekte.htm) referenced in the macro (e.g., a symbol library) is not in the current project, the macro may not be displayed. In this case you have the option of synchronizing and / or completing the [project data](Glossary_o_projektdaten.htm) under Utilities > Master data. In addition, you can synchronize project parts data with the [master data](Glossary_o_stammdaten.htm) parts by selecting the menu [items](Glossary_o_bauteile.htm) Utilities > Parts > Parts database --> current project .

See also

[Macros](macrosgui_k_start.htm)

[Creating Macros](macrosgui_h_makroserzeugen.htm)

[Generating Macros from DXF / DWG Files](macrosgui_h_makrosausdxf.htm)

[Master Data: Managing Macros](xmasterdatasettingsgui_h_makrosverwalten.htm)