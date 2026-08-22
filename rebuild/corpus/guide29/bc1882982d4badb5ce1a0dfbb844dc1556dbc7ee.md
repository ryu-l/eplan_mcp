# Macro Navigator

In a macro file [macros](Glossary_o_makros.htm) can be stored in different [representation types](Glossary_o_darstellungsarten.htm) and per representation type in several [variants](Glossary_o_varianten.htm) â depending on whether they are window, symbol page or 3D macros. You can use the macro navigator for a well-structured display and management of macros in a project. In the tree of this navigator the macros are displayed in a hierarchical structure. The representation types and variants are displayed below a node for a macro.

- In a macro project all the representation types and variants are displayed that are stored later during the generation in a macro file for a prepared macro. This applies to all macro types.
- In a schematic project only the inserted representation types and variants of a window and / or [symbol macros](Glossary_o_symbolmakros.htm) are displayed and not all the variants existing in macro file.

If you mark a macro in the macro navigator, the corresponding page / [layout space](Glossary_o_bauraum.htm) of the macro project is displayed in the graphical preview.

The following is possible:

- You can use the popup menu to view and edit the [properties](Glossary_o_eigenschaften.htm) of the macro. In the process the respective [property dialog](Glossary_o_eigenschaftendialog.htm) is opened (for example the property dialog of a macro box for a window macro).
- By means of the popup menu item Go to (graphic) you jump into the graphical editor or into a layout space and can there edit the respective schematic section or the respective 3D [object types](Glossary_o_objekttypen.htm).
- Filters can be used to limit the display to the macros that fulfill specific criteria. This allows you to, for example, have only the macros of a specific representation type displayed and subsequently generated automatically.
- You can synchronize the selection between the [objects](Glossary_o_objekte.htm) for the macros in the graphical editor / layout space and the macro navigator.
- In a macro project you can automatically [generate](Glossary_o_erzeugen.htm) macros from the prepared macros displayed in the macro navigator.
- You can use the macro navigator in schematic projects to update several macros existing in a project with the data from the associated macro files by means of the popup menu item Update macros.

### Placeholder objects in the Macro Navigator

The [placeholder objects](Glossary_o_platzhalterobjekte.htm) available in a macro are displayed below the hierarchy level of the respective macro variant (![](../Pictures/Gui/ALL/cabinetgui_placeholder_as.png) icon) in the tree of the macro navigator. A multiple selection of placeholder objects is possible, [block editing](Glossary_o_blockbearbeitung.htm) only under certain [conditions](macrosgui_h_platzhalterobjekteerzeugen.htm#BlockbearbeitungPlatzhalterobjekte). Value sets for the placeholder objects can be selected from the popup menu and their properties edited.

### Inserting Macros from Macro Navigator Using Drag & Drop

You can insert the window and symbol macros of a macro project from the macro navigator to the open project pages of another macro or schematic project or the same macro project using Drag & Drop.

This action is possible both for macros with the type of usage "Defining" as well as for macros with the type of usage "Not specified". You can drag 3D macros using Drag & Drop into an opened layout space in the same way. The selection of a different macro variant is not possible when inserting via Drag & Drop. You also cannot select multiple macros.

Alternatively you can also execute the action in the macro navigator via the Insert macro popup menu item.

![](../Pictures/Gui/ALL/note.png)Note:

Please also note that when inserting via Drag & Drop or via the Insert macro popup menu item, the status of the macro in the macro project and not the saved status of the macro in the macro file is used. If you update a macro that was inserted this way, the status that was saved in the macro file is used.

See also

[Macro projects](macrosgui_k_makroprojekte.htm)

[Creating Macro Projects](macrosgui_h_makroprojekteerstellen.htm)

[Using Macro Boxes](macrosgui_h_makrokasten.htm)

[Generating Macros from a Macro Project](macrosgui_h_makrosausmakroprojekt.htm)

[Dialog Macros - <Project name>](macrosgui_d_makronavigator.htm)

[Drag & Drop](userinterface_k_dragdropfunktionen.htm)