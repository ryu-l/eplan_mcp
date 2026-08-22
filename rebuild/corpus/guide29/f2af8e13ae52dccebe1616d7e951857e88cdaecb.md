# Dialog Placeholder objects - <Project name>

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have opened a project and inserted [placeholder objects](Glossary_o_platzhalterobjekte.htm) into this project. Project data > Project options > Placeholder objects.

All placeholder [objects](Glossary_o_objekte.htm) in the project are listed in this dialog. You can use the popup menu to edit the [properties](Glossary_o_eigenschaften.htm) of the placeholder objects and assign value sets to them.

Overview of the main dialog elements:

The placeholder objects are displayed in the Tree tab sorted hierarchically according to "<Name>" and "Placement (<Description>)". (This the case for the default configuration.) In the process placeholder objects with the same name are combined.

![](../Pictures/Gui/ALL/note.png)Note:

In contrast to the name that is identifying and is therefore not multilingual, the description can be used for additional information that can also be displayed in a foreign language. The corresponding multi-language text is entered in the Placeholder object tab.

In the List tab, the name, description, placement and most recently selected value set are displayed as standard. The displayed properties can be configured using the popup menu.

Filter:

This drop-down list displays all the available [filters](Glossary_o_filter.htm). A selected filter is automatically activated and is applied to both the tree and the list view. The "- Not activated -" entry deactivates the filter and causes an unfiltered display of the data. Click [...] to open the [Filter](modaldialogsdb_d_filternnach.htm) dialog. Here you can [create](Glossary_o_erstellen.htm), edit, delete, copy, export, import, and manage filters.

The popup menu of the Filter drop-down list contains the following entries:

- Deactivate: This popup menu item is available if a filter has been set: Resets the filter setting to the "- Not activated -" entry.
- Activate <filter name>: This popup menu item is available if the filter setting is "- Not activated -": Reactivates the last active filter.

This allows you to toggle rapidly between the unfiltered representation and a representation filtered in accordance with your requirements.

Value: <Property>:

Use this field, via [Quick input](modaldialogsdb_k_filter.htm#I_Schnelleingabe), to adjust quickly the value of a filter criterion for a defined and activated filter.

Popup menu:

| Menu item | Meaning |
| --- | --- |
| Select all (list only) | Selects all of the entries in the list. |
| Adjust column width (list only) | Adjusts the width of all table columns so that both the headings and column contents are fully legible. |
| Assign value set | Opens the Select value set - < Placeholder name> dialog, allowing you to assign a value set to the selected placeholder objects. |
| Select associated objects | Selects all objects belonging to the current placeholder object in the graphical editor. |
| Edit revision marker | This menu item allows you to edit the [revision marker texts](Glossary_o_revisionsmarkierungstexte.htm) and their format. This menu item is only available when a changed object in a revision is selected. |
| Delete revision marker | This menu item allows you to delete the revision marker texts. This menu item is only available when a changed object in a revision is selected. |
| Go to (graphic) | Shows the selected placeholder object in the graphical editor. |
| Configure representation | Opens the Configure representation dialog, where you define which properties are to be displayed in the list and tree view. |
| Properties | Opens the Placeholder object dialog. Allows you to edit the properties of the placeholder object. |

See also

[Creating Placeholder Objects](macrosgui_h_platzhalterobjekteerzeugen.htm)

[Extending Placeholder Objects](macrosgui_h_platzhalterobjekteerweitern.htm)