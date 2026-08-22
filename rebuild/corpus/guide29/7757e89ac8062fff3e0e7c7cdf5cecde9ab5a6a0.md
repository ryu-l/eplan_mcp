# Displaying Revision Markers

Revision markers are automatically generated and displayed in the project. There are two different ways to do this:

- If you have generated a revision and are still working in the revision project, changes are automatically marked ("Change tracking").
- If you have compared the [properties](Glossary_o_eigenschaften.htm) of two [projects](Glossary_o_projekte.htm), changes are entered in the revision results list and also automatically marked in the project. If you have deleted these markers, you can regenerate the [revision markers](Glossary_o_revisionsmarkierungen.htm) from the list of results so that the changes can be displayed again in the project. By default, the revision results list is overwritten during each new project comparison.

Revision changes in the schematic are shown with graphical markers. You specify the appearance and the size of this graphics in the project [settings](Glossary_o_einstellungen.htm) (under Options > Settings > Projects > "Project name" > Management > Revision (graphical representation)) in the Settings: Revision dialog.

Changes in the reports are also displayed using graphical markers. The changed [objects](Glossary_o_objekte.htm) are then marked on the corresponding [report pages](Glossary_o_auswertungsseiten.htm).

Changes in properties are shown with marker text entered into the Revision marker (change tracking) or Revision marker (from property comparison) properties. In addition, the modified object is shown with a graphical marker.

In [change tracking](Glossary_o_aenderungsverfolgung.htm), this text is generated automatically, but it can be changed. Formatting is also specified in he project settings in the Settings: Revision (change tracking) dialog.

In a project comparison, you enter this text in the Compare properties of projects dialog.

![](../Pictures/Gui/ALL/info.png)Tip:

If no revision data and no revision markers are to be included in copying and to be pasted into the target project, during the copying and pasting of schematic areas, pages or layout spaces as well as during the insertion of [macros](Glossary_o_makros.htm), deactivate the user setting Retain revision data and revision markers during inserting.

### Deletion markers

If the While deleting create deletion markers and list deleted pages check box is selected under Options > Settings > Projects > "Project name" > Management > Revision (change tracking), the deleted objects (components, texts, etc.) on the project pages of a revision project are indicated by a revision marker and a special object - the deletion marker. The set color for deleted objects is used for the revision marker here. The deletion marker is placed in the same position as the previously existing object and has a [property dialog](Glossary_o_eigenschaftendialog.htm).

Deletion markers can also be generated in a property comparison of projects. To do this, the Create deletion markers for deleted objects check box must be selected in the Compare properties of projects dialog.

### Display deleted pages

If the While deleting create deletion markers and list deleted pages check box is selected, then information about the deleted pages will be saved when the pages of a revision project are deleted. You can display a relevant list using the Deleted pages dialog. This dialog can be accessed via the Utilities > Revision control > Change tracking > Deleted pages menu [items](Glossary_o_bauteile.htm). The data displayed here cannot be modified.

Deleted pages can also be displayed in the revision overview: If the [form](Glossary_o_verlauf.htm) property Revision output with deleted pages ([ID](Glossary_o_id.htm) 13088) is selected, deleted pages are output in the revision overview. The "Pages" option must also be selected for the Revision output type (ID 13106) property.

See also

[Revision Control: Principle](revisionmgtgui_k_prinzip.htm)

[Displaying or Hiding Revision Markers](revisionmgtgui_h_revmarkierungen_anzeigen.htm)

[Editing Deletion Markers in Revision Projects](revisionmgtgui_h_loeschzeichenbearbeiten.htm)

[Deleting Deletion Markers in Projects with Property Comparison](revisionmgtgui_h_loeschzeichenentfernen.htm)

[Restoring Deleted Revision Markers](revisionmgtgui_h_revmarkierungenerzeugen.htm)

[Dialog Settings: General (user, display)](macrosgui_d_einstellzwischablage.htm)