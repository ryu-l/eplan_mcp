# Dialog Structure identifier settings

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have opened a project. You have generated a reference project. Utilities > Revision control > Property comparison of projects > Compare projects. In the Compare properties of projects dialog, click [...] beside the Structure identifier setting field.

In this dialog, you specify which [structure identifiers](Glossary_o_strukturkennzeichen.htm) in the reference project are to be replaced by which structure identifiers from the current project, and you can save these [settings](Glossary_o_einstellungen.htm) in a separate scheme. The specified structure identifiers are then no longer seen as different during a property comparison of [projects](Glossary_o_projekte.htm).

Overview of the main dialog elements:

Scheme:

Select the scheme that you wish to use or edit from the drop-down list. You can also use the adjacent [toolbar](schemeconfig_m_schemaschaltflaechen.htm) for this purpose.

Project / reference project table:

The following buttons are available on the Toolbar above the table:

| Button | Meaning |
| --- | --- |
| (New) | Opens the Criteria selection dialog for selecting an identifier block. Enables you to specify a structure identifier in the table in each row. |
| (Delete) | Deletes the currently selected line(s). Multiple selection is possible. |

- Identifier block: The identifier block is shown here. Click [...] in the cell to open the Criteria selection dialog and select a different identifier block if required.
- Designation (project): Here you specify which structure identifier was renamed in the current project. Click [...] in the cell to select a structure identifier from the current project in the dialog that opens.
- Designation (reference project): Here you specify which designation a renamed structure identifier had in the reference project. Click [...] in the cell to select a structure identifier from the reference project in the dialog that opens.
- Status: When the renamed structure identifier is specified, the system checks to see whether a structure identifier from the reference project is assigned to the structure identifier from the current project. If this is the case, a green icon appears ![](../Pictures/Gui/ALL/all_statusok_as.png). In the rows where structure identifiers are missing, a yellow icon is shown ![](../Pictures/Gui/ALL/all_statusnotok_as.png).

See also

[Comparing Projects](revisionmgtgui_h_revvergleichen.htm)