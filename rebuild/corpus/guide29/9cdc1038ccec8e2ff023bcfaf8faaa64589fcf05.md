# Special Features of the Navigators

The different [navigators](Glossary_o_navigatoren.htm) offer different views of the [project data](Glossary_o_projektdaten.htm). For example, the device navigator displays all [functions](Glossary_o_funktionen.htm) except functions for [representation types](Glossary_o_darstellungsarten.htm) "External" and "Graphic", whereas the cable navigator only displays cables and [shields](Glossary_o_abschirmungen.htm) and the terminal strip navigator only displays terminal strips and terminals.

![](../Pictures/Gui/ALL/note.png)Notes:

- Note that the navigators only display subsets of the project. For example, the device navigator does not display any functions for representation types "External" or "Graphic". (External and graphic functions are not [part](Glossary_o_artikel.htm) of the project and are not reported.)  
  If criteria are specified for a filter in a navigator that cannot be displayed in the respective navigator (for example the value "External" for the "Representation type" criterion), it is not possible to filter to these [objects](Glossary_o_objekte.htm).
- In the navigators, leading zeros of the counter are ignored during sorting. The sorting of pages and functions is not alphanumeric in this case.

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

A project contains terminal strip [designations](Glossary_o_bezeichnungen.htm) with a different number of leading zeros. In the terminal strip navigator, the terminal strips are sorted in the following sequence:

X001311
  
X1312
  
X01313
  
X1511
  
X1611.

In the case of alphanumeric sorting (such as, e.g., in MS Excel), the sequence would be:

X001311
  
X01313
  
X1312
  
X1511
  
X1611.

### Display if multiple projects are open

The data from several [projects](Glossary_o_projekte.htm) can be displayed at the same time in the navigators. If several projects are open, then the first level of the tree view also displays the project name. For orientation purposes, the project name is also displayed in the navigator title bar.

The current project is identified from the selection in the page navigator; it does matter which window has the focus and which objects have been selected there. Therefore the project name is always updated but the page name is not updated until another page is opened.

### Tree view selection options

If you have selected a level in the tree view, then all objects below this level are also selected. The particular objects that can be selected depend on the particular navigator being used.

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

You have opened multiple projects. Now open the page navigator and the terminal strip navigator. Selecting a project in the page navigator also selects all pages and the [devices](Glossary_o_betriebsmittel.htm) placed on these pages. However, if you select a project in the terminal strip navigator, then only the terminal strips and terminals in the project are selected because, in a certain sense, the other devices are already filtered out.

If you have defined and activated a filter in a navigator then this filter is taken into account in the selection process. Even when a project level is selected, then only the filtered data is contained in the selection.

### Editing possibilities

In the different navigators, only the project data that can be displayed or selected in a given navigator can be edited in this navigator.

- From the page navigator you can edit the [properties](Glossary_o_eigenschaften.htm) of pages and functions placed on these pages.
- From the device navigator you can edit the properties of all functions existing in the project.
- From the terminal strip navigator you can edit the properties of terminal strips and terminals. However, you cannot edit the properties of cables or [plugs](Glossary_o_stecker.htm) from here.
- From the [cable](Glossary_o_kabel.htm) navigator you can edit the properties of cables and shields, but not the properties of terminal strips or plugs. The same principle applies to the other navigators.

If you have defined and activated a filter in a navigator, then only the selected and filtered data can be edited in the dialog. This also applies when a project is selected.

An editing action can only be performed when suitable data has been selected. If this is not the case, then a message is displayed.

#### Behavior of the setting "Apply to entire project"

With certain editing [actions](Glossary_o_aktionen.htm), e.g. numbering, you can extend the editing action beyond the current selection and apply it to the entire project. The corresponding dialogs contain the Apply to entire project check box.

![](../Pictures/Gui/ALL/note.png)Note:

In the special project data navigators for terminal strips, plugs, PLC data, etc., not only the functions displayed there are edited, but all devices of the project. In the page navigator, the [unplaced functions](Glossary_o_nicht_platziertefunktionen.htm), which are normally not contained in the selection, are also processed. Any filter that may be set is not taken into account.

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

You have selected a page in the page navigator and then select the menu item Project data > Devices > Number. In the Number dialog, select the check box Apply to entire project. All devices in the project are then numbered, including the unplaced ones. If the check box is deselected, only the placed devices on the selected page will be numbered.

You have selected three terminal strips in the terminal strip navigator and then select the menu [items](Glossary_o_bauteile.htm) Project data > Devices > Number. In the Number dialog, select the check box Apply to entire project. All devices of the project will be numbered. If this check box is deselected, then only the selected terminal strips are numbered.

You have selected a project in the terminal strip navigator and also defined a filter criterion stating that only the [mounting location](Glossary_o_einbauort.htm) ET1 is to be taken into account. The filter is active. You select the menu item Project data > Devices > Number. If the Apply to entire project check box in the Number dialog is selected, then all devices in the project are numbered. In this case, the filter is not taken into account. If the check box is deselected, then only the terminal strips of the ET1 mounting location are numbered.

### Navigators and message management

After the execution of [check runs](Glossary_o_prueflaeufe.htm), faulty functions in the navigators are identified with an exclamation mark for functions. Select a function there and then activate the Selection check box in the Message management - <Project name> dialog, which causes only the messages relating to this function to be displayed in the message management.

If you select the check box while you are in the page navigator, then only the messages relating to the objects on the respective pages are displayed in the message management; if you select the check box from the graphical editor, only the messages relating to the currently selected [component](Glossary_o_schaltzeichen.htm), [connection definition points](Glossary_o_verbindungsdefinitionspunkte.htm), and [interruption points](Glossary_o_abbruchstellen.htm) are displayed.

See also

[User Interface Elements](userinterface_k_hintergrund.htm)

[Icons in the Navigators](userinterface_k_iconsnavigatoren.htm)