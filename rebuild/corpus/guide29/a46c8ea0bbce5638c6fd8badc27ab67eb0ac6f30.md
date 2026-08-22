# Dialog Check project

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have opened a project. You have selected one or more pages or a project in the page navigator, or you have opened a page in the graphical editor. Project data > Messages > Check project.

In this dialog, select a scheme for the testing of [project data](Glossary_o_projektdaten.htm). The scheme specifies which individual checks will be performed and how the messages are classified.

The following dialog elements are available:

Settings:

Select a scheme from the drop-down list. Click [...] to open the [Settings: Messages and checks](xesinspectiongui_d_einstellungenmeldungen.htm) dialog, where you can specify your own scheme for the display of [check run messages](Glossary_o_prueflaufmeldungen.htm).

Apply to entire project:

Activate this check box to extend the check to the entire project.  
If a project was already highlighted, this option will be set as a default, and cannot be deactivated.

Check only completed messages:

If this check box is activated, the subsequent offline check run will check only messages for which the Completed check box has been activated in message management. All non-completed messages remain unchanged in the message database.

In this case, all other [settings](Glossary_o_einstellungen.htm) for the check run or a selection made in the [navigators](Glossary_o_navigatoren.htm) will be ignored. The Settings field and the Apply to entire project check box are therefore grayed out.

See also

[Error Checking](msgmanagementgui_k_prueflaufprinzip.htm)

[Configuring Project Checks](msgmanagementgui_h_konfigurieren.htm)

[Checking Project Data](msgmanagementgui_h_prueflauf.htm)