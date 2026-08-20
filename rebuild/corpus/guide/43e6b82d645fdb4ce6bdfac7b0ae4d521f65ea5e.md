# Dialog Select attached documents

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have selected a project or pages in the page navigator. You have inserted external documents via hyperlinks or have entered them at parts. File > Print > Group box Scope of printing > [Select attached documents].

All attached documents linked in the project are listed in this dialog. attached documents are external documents inserted into schematic pages via hyperlinks or entered into the parts used on the page. From these documents, you select those that are to be printed. In order for Attached documents to be printed, the files must be located on a local drive or a network drive to which you have access.

![](../Pictures/Gui/ALL/note.png)Note:

Attached documents are only printed if they are contained in the scope of printing. If you have selected the Only attached documents option for the scope of printing, the following linked documents are not taken into consideration during printing

- Pages of page type "External document". These pages are printed out when printing projects / pages.
- Linked documents on report pages. These attached documents are covered by the parts that have already been taken into account.
- Documents linked via the http protocol (e.g., Internet pages).

Overview of the main dialog elements:

All attached documents linked in the project are listed in this table. The table contains the following columns:

- Document: The file name of the external document including file path are shown here.
- Page, part: The page names or part numbers for which attached documents have been found are listed here. For documents that are linked in a project multiple times, the respective page names or part numbers are separately listed separated by commas.
- Print: If the check box in a cell is activated, the corresponding document is printed. If the check box is deselected, the document is not printed.

Popup menu:

The popup menu provides - depending on the field type (e.g. date, integer, multilingual) - the following menu items that are, depending on the situation, available for influencing the table or editing the values in the fields. You can find an overview of these popup menu items in the section [Popup menu items](userinterface_m_kontextmenu.htm).

See also

[Printing Attached Documents](printgui_h_begleitdokumente.htm)

[Print](printgui_k_start.htm)