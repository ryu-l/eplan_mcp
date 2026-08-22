# Symbol Editor

Symbols are needed to simplify the process of drawing the schematic. They contain a variety of information such as graphical elements, [connecting points](Glossary_o_anschlusspunkte.htm), symbol group assignment, logic, etc. The relationship between a symbol and a function can look like this:

- The symbol does not represent a function, such as an angle or a T-node.
- The symbol represents one function, such as an NO contact or an NC contact.
- The symbol represents several [functions](Glossary_o_funktionen.htm), such as a motor overload switch or a triple fuse.
- The symbol represents one part of a function, such as a device connection point or a change-over contact hook.

The [symbol libraries](Glossary_o_symbolbibliotheken.htm) are used to manage the [symbols](Glossary_o_symbole.htm). A symbol library can contain an unlimited number of symbols. When editing a symbol only the changed symbol is opened and saved, not the entire library. This minimizes the problems that could arise when multiple users are working in one library simultaneously.

When working with the [symbol editor](Glossary_o_symboleditor.htm) you will need to pay attention to a number of special differences between it and the graphical editor:

- Because the symbol editor does not use referencing symbols, the symbols are broken up when inserted.
- Only the standard [layers](Glossary_o_ebenen.htm) can be used. Elements on open layers must be adjusted when they are inserted. This applies especially for [macros](Glossary_o_makros.htm), [DXF](Glossary_o_dxf.htm) / [DWG](Glossary_o_dwg.htm), and the Clipboard.

Several symbol [properties](Glossary_o_eigenschaften.htm) can be preset via the project [settings](Glossary_o_einstellungen.htm) (Options > Settings > Projects). To use these when creating symbols as well, the symbol editor must be able to access them. For this reason, [master data](Glossary_o_stammdaten.htm) such as symbols can only be edited when a project is open.

See also

[Symbol Editor: Functionality](symboleditorgui_k_arbeitsweise.htm)