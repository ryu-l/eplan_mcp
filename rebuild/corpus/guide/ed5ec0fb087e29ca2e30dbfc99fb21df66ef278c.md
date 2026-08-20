# Dialog Property placement

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have opened a project. You have either opened or created a symbol in the symbol editor (Tab Master data > Command group Symbols > Drop-down button Symbol > [Open] or New). Tab Edit > Command group Symbol > Drop-down button Other > Placed properties.

In this dialog you select a property placement (for example for connection point designation, connection point description, DT, function text, etc.) and specify its position, direction and format.

Overview of the main dialog elements:

Property arrangement:

In the drop-down list, different predefined assignment configurations are offered for selection. These configurations are stored on the symbol with their names. With the Edit property arrangements command you have the possibility to generate own property arrangements (Tab Edit > Command group View > ![](../Pictures/Gui/ALL/ribbon_editpropertyarrangements_as.png) (Edit property arrangements)).

---

Tab Components

In the Components tab, specify which properties are placed and displayed together with the symbol. If you have selected a property, you can edit its display properties in the right side of the dialog.

---

Contact image tab

In the Contact image tab you specify whether a contact image is displayed for the symbol. To this purpose you select the alignment of the contact image via ![](../Pictures/Gui/ALL/all_new_as.png) (New) in the dialog Generate contact image:

- In path: The contact image â depending on the selected plot frame â is displayed below or right on the page in the schematic path of the component.
- On component: The contact image is displayed next to the component.

---

Property / Assignment:

If you have selected a property, you can edit its display properties in the table in the right-hand section of the dialog. The hierarchy levels Format, Text box, Alignment box, Value / unit, and Position are available to this purpose. These can be opened by clicking the ![](../Pictures/Gui/ALL/all_expand_hierarchy_as.png) symbol.

To be able to edit the settings for the contact image in the Contact tab you must select one of the contact image alignments ("In path", "On component"). To this purpose only the hierarchy level Position is available in the symbol editor.

The settings described in the following sections are available for the display properties:

- [Display Properties: Placed Property](devicetaggui_r_anzeigeeigenschaften.htm)
- [Display Properties: Contact Image](devicetaggui_r_anzeigekontaktspiegel.htm)

Popup menu:

The popup menu provides - depending on the field type (e.g. date, integer, multilingual) - the following menu items that are, depending on the situation, available for influencing the table or editing the values in the fields. You can find an overview of these popup menu items in the section [Popup menu items](userinterface_m_kontextmenu.htm).

![](../Pictures/Gui/ALL/note.png)Note:

Properties cannot be placed on connection symbols (angles, T-nodes, double junctions) and existing property placements will be removed when you save / close the symbol editor. This applies especially to connecting points that automatically possess a property placement (namely, the connection point description / designation).

See also

[Symbol Editor](symboleditorgui_k_start.htm)

[Creating Symbols](symboleditorgui_h_symboleanlegen.htm)