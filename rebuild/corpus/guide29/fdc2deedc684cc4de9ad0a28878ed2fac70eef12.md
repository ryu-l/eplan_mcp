# Tab General

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have installed the hose line configurator as an add-on variant of EPLAN Fluid. You have started EPLAN Fluid and the hose line configurator.

- Select the menu [items](Glossary_o_bauteile.htm) Options > Settings > User > Add-ons > Hose line configurator in EPLAN Fluid and click in the General tab in the subsequent dialog.
- Or select the menu items Extras > Settings in the Configure hose lines dialog of the hose line configurator and click in the General tab in the subsequent dialog.

Or you have installed the hose line configurator as a stand-alone variant and started the program.

- Select the menu items Options > Settings > User > Add-ons > Hose line configurator in the hose line configurator and click in the General tab in the subsequent dialog.

In this tab you specify the general [settings](Glossary_o_einstellungen.htm) for the hose line configurator.

Overview of the main dialog elements:

Prefix:

Enter any character or any string in this field.

Each hose line created in the hose line configurator has a temporary DT assigned to it that consists of an assigned prefix and a sequential number. The prefix serves the identification of newly created [hose lines](Glossary_o_schlauchleitungen.htm) that do not yet have a final DT.

![](../Pictures/Gui/ALL/note.png)Note:

If you select the default scheme DIN 20066\_2012-01, the entry "H" is preset as the prefix in this field.

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

You [create](Glossary_o_erstellen.htm) two new hose [lines](Glossary_o_leitungen.htm) in the hose line configurator. You have selected the preset value H as the prefix. The first newly created hose line has the temporary DT H1 assigned to it, the second hose line the temporary DT H2.

Part template:

A [project part](Glossary_o_projektartikel.htm) or a [part](Glossary_o_artikel.htm) reference can be created optionally for each created [type code](Glossary_o_typencode.htm).

You can influence this behavior as follows by using the Part template field: If you do not enter a value in the Part template field, a part reference is created. If, on the other hand, you have assigned a value to the field, a project part is created.

If you use the hose line configurator as an add-on variant of EPLAN Fluid, you can use the [...] button available in the table cells to access the part selection and there select the desired part template.

![](../Pictures/Gui/ALL/note.png)Note:

If you select the default scheme DIN 20066\_2012-01, the entry "Fluid-Hose-1" is preset in this field.

Format type code:

You can use this field to define the display format for the type code of the hose lines, thus determining the composition of the type code components. The created type code is output in the Edit <...> dialog.

Through the [...] button you access the dialog [Format: Property](fluidhoseconfiggui_d_formattypencode.htm) in which you select the [format elements](Glossary_o_formatelemente.htm) of the type code in the [form](Glossary_o_verlauf.htm) of [properties](Glossary_o_eigenschaften.htm) and separators and can position these in the desired configuration. By default the display format for the generation of a type code in accordance with the standard DIN 20066 is offered in this dialog. It is also possible to define type codes deviating from the DIN standard through the selection of other format element combinations and / or by the supplementing of free properties. This allows you, for example, to order hose lines in accordance with manufacturer-specific specifications.

Measuring unit for hose line length:

Select the desired measuring unit for displaying the hose line length from the drop-down list. The measuring unit does not appear in the created type code.

![](../Pictures/Gui/ALL/note.png)Note:

If you select the default scheme DIN 20066\_2012-01, the entry "mm" is preset in this field.

Popup menu:

The popup menu provides - depending on the field type (e.g. date, integer, multilingual) - the following menu items that are, depending on the situation, available for influencing the table or editing the values in the fields. You can find an overview of these popup menu items in the section [Popup menu items](userinterface_m_kontextmenu.htm).