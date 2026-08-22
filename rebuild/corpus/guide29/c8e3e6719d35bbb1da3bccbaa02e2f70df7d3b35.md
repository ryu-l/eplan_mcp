# Dialog Settings: Copper bending (user)

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

Options > Settings > User > Graphical editing > Copper bending.

Use this dialog to define the behavior of automatic inheriting of [drill holes](Glossary_o_bohrungen.htm) in copper components.

Overview of the main dialog elements:

Automatic multiple cut-out:

When equipping copper [items](Glossary_o_bauteile.htm), [cut-outs](Glossary_o_durchbrueche.htm) can be referenced automatically from one copper item to another. If a copper item is placed on the mounting surface of another copper item, and in the area of the overlap, there is a cut-out, such a cut-out will be referenced automatically to the newly placed copper item.

The inheriting of cut-outs from a drilling pattern is controlled by the Multiple cut-out possible property of [part](Glossary_o_artikel.htm) placement. This property is set only in connection with the placement of any part placement on a copper item.

If the Automatic multiple cut-out check box is activated, this property will be turned on upon placement, and referencing occurs.

Automatically update multiple cut-outs:

The inheritance of cut-outs can be affected by different [actions](Glossary_o_aktionen.htm) that modify copper items, so that they are no longer displayed correctly. If this check box is activated, an update is made after each modification of the cut-outs.

![](../Pictures/Gui/ALL/note.png)Note:

The use of the Automatically update multiple cut-outs setting can affect the work speed in [projects](Glossary_o_projekte.htm) wit many copper items and many inherited cut-outs. In such a case, it is advisable to deactivate this setting and to run a manual update, if necessary, using the menu items Edit > Graphic > Update multiple cut-outs.

See also

[Inheriting Drilling Pattern Automatically or Manually](copper_h_bohrbildvererben.htm)