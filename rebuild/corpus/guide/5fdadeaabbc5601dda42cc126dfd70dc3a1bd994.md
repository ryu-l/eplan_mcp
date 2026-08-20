# Defined Working Sections: Principle

The division into defined working sections is accomplished by filter schemes. For filtering, all properties for structure identifiers are available. Any combinations of structure identifiers existing within the project can be used as filtering criteria. In addition you can use the Trade (Defined working sections) property to filter by certain trades on pages, layout spaces, functions, and connections.

Several filter criteria can be linked to each other logically. This way, for example, you can simultaneously filter by a specific structure identifier and a specific trade.

Placeholders (such as "\*" and "?") can be used for the values of the filter criteria. For example, this makes it possible to capture structure identifiers with lower-level substructures in a single filter expression.

### Open projects with active selection of defined working sections

If the selection of defined working sections has been activated for a project, when you open this project, you will see the Define working sections dialog immediately.

If you access a project via a network with several users, the All editors column will show you whether another user has already defined a working section for this project. But this will not show you whether another user has already opened the project.

If the program is restarted and one of the automatically opened projects is divided into defined working sections, a corresponding message is displayed.

### Editing in the entire project

The Eplan platform contains editing actions (e.g., the numbering of devices) that you do not execute only for the current selection but that you can also extend to the entire project. The dialogs allowing this contain the Apply to entire project check box.

When you work in a project with defined working sections, such editing actions, despite an active setting, will not affect the entire project, but only your defined working section.

If you still want to execute the editing for the entire project, you will have to extend your defined working section temporarily to the entire project. To this purpose select the commands File > Collaboration > Command group Defined working sections > Activate and activate the check box Entire project. Subsequently, the entire project is displayed again in the project data navigators. After you have completed the action, exit the temporary editing in the entire project by selecting the command again and deactivate the check box.

![](../Pictures/Gui/ALL/info.png)Tip:

Using the Go to (graphic) popup menu item, you can jump to an object (page / layout space) that does not belong to your defined working section. This way, for example, you can jump from a report page to the associated schematic page and make modifications there, even if the schematic page is not part of your defined working section.

#### Update connections

A manually executed or automatic connection update only affects the current defined working section. In this context, a connection belongs to a defined working section as soon as a target of such connection belongs to the defined working section.

Please note that non-current connections can result in incorrect reports (for example, in case of connection diagrams). To update a connection for the entire project, you must first extend your defined working section temporarily to the entire project.

### Defined working sections report

The following commands are available to report working sections: Tab Tools > Command group Reports > Generate project reports. This command allows you to evaluate all reports that lie fully or partially in your defined working section.

Any report pages outside of your defined working section cannot be deleted, created or updated. This also applies to the model views.

Report blocks are either updated entirely or not at all. For a report block to be updated its start page has to be inside your defined working section.

To generate a report of the entire project, you must first extend your defined working section temporarily to the entire project.

We recommend that you output the reports of your defined working section in a separate report project. The reports of the entire project can be output either in another report project or be contained in the project itself, and, for example, they can be generated and updated overnight.

### Display of defined working sections in the multi-user monitor

When working in multi-user operation, you can see in the multi-user monitor whether another user has selected defined working sections in an opened project.

In the Own opened projects in multi-user operation table, the structure identifiers are displayed in the Area column that have been defined by another user in the respective project as a defined working section. If another user temporarily works in the entire project, the Area column will show the entry "No limitations".

See also

[Dividing Projects into Defined Working Sections](workingsection_h_bereichedefinieren.htm)

[Outputting Reports in Another Project](formgeneratorgui_h_inanderesprojekt.htm)