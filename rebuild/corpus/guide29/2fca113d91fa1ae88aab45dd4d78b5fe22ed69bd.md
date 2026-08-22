# Connection Point Designations and Descriptions

In EPLAN you have the option of creating multiple sets of [connection point designations](Glossary_o_anschlussbezeichnungen.htm) and descriptions. These can also be imported or exported. Connection [designations](Glossary_o_bezeichnungen.htm) and descriptions are saved with references to [function definitions](Glossary_o_funktionsdefinitionen.htm) when exported and when they are imported the function definitions are assigned again.

The logic information is located in the same file as the function definitions themselves. It is provided by EPLAN Software & Service, and you can't change it. You may, however, [create](Glossary_o_erstellen.htm) [symbol macros](Glossary_o_symbolmakros.htm) for special logic [settings](Glossary_o_einstellungen.htm).

Connection point designations

You can define up to 10 connection point designation recommendations for every function definition connection point. This data is stored in the individual function definitions The connection point designation identifies the connection point.

When creating a function, the connection point designations are prepopulated with the connection point designation "1". In the [Connection point logic](xfctdefbrowsergui_d_anschlusslogik.htm) dialog you can edit the connection point designations. Select an entry from the drop-down list or manually enter your own connection point designation. Connection point designations are always entered in the function and are not referenced.

![](../Pictures/Gui/ALL/example.png) [![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

You create a function with the "NO contact" function definition. Connection point designations are prepopulated with 1, 2. The sets of connection point designations you predefined are available in a drop-down list, for example, 13, 14 or 23, 24 or 33, 34. Select a set from those, for example 23, 24. The list with the sets of connection point designations is saved on the function definition while the selected connection point designations (in this case, 23, 24) are saved on the function.

Connection point descriptions

You can define up to 10 connection point description recommendations for every function definition connection point. This data is stored in the individual function definitions The connection point description is an additional, non-identifying entry.

### Functions with a variable number of connection points

Function definitions exist for a specified number of [connection points](Glossary_o_anschluesse.htm) and a variable number of connection points. "n" is entered for these as the number of connection points. The last connection point is treated specially if "z" is entered as the connection point number.

If you select a function definition for which the number of connection points is "n", then the number of connection points for the function follows the symbol used. If the connection point "z" is defined for the function definition, then its data (logic, ...) is assigned to the last connection point of the function. All other connection points contain the data from connection point "n". For [unplaced functions](Glossary_o_nicht_platziertefunktionen.htm) (without symbol), for example in the [devices](Glossary_o_betriebsmittel.htm) navigator, you have to specify the number of connection points yourself.

The variable [functions](Glossary_o_funktionen.htm) are to be used when there is no other suitable function. You will also have to specify logic information like potential transfer and [target tracking](Glossary_o_zielverfolgung.htm) in the function yourself. This information cannot be predefined because the number of connection points was not known. There are variable functions in every category so that you can always achieve the desired reporting behavior.

### Function definitions for single-line representation

There are special function definitions for single-line representation. There are also single-line function definitions for the variable function definitions.

There are no special single-line function definitions for terminals and [plugs](Glossary_o_stecker.htm). Normal terminals and plugs are used here that are then correspondingly reported.

See also

[Functions: Principle](xfctdefbrowsergui_k_prinzip.htm)

[Your Own Connection Point Designations and Identifiers](fctdeflibdataexchangegui_k_start.htm)

[Creating Your Own Connection Point Designations and Descriptions](fctdeflibdataexchangegui_h_eigenanschlussbezeichnungen.htm)

[Exporting Your Own Sets of Identifiers, Connection Point Designations, and Connection Point Descriptions](fctdeflibdataexchangegui_h_eigenesaetzeexportieren.htm)

[Importing Your Own Sets of Identifiers, Connection Point Designations, and Connection Point Descriptions](fctdeflibdataexchangegui_h_eigenesaetzeimportieren.htm)