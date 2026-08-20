# Project Page View

In the page navigator you can see all of the Eplan user page properties, open pages, and print pages. In addition to this - depending on the user rights - pages from one project can be edited, i.e. copy, delete, or modify the properties of pages. Please note that these editing functions are only available when pages in the same project are selected; several pages from different projects cannot be edited simultaneously.

When Eplan is started, the last active page in the page navigator is selected. The page names are saved on a per-user basis. If the page is unavailable in the open project, then the first page is selected.

The Filter enables you to limit the number of displayed pages. The filter settings apply equally to the tree view and the list view.

### Tree view

In the tree view, the pages are displayed hierarchically by page type and structure identifier (such as function designation, location designation, etc.).

- Several projects with different project structures can be displayed simultaneously.
- You can select multiple pages.
- Graphical, logical, and report pages are represented by different icons. Structure identifiers are also represented by different icons.
- Opened pages are displayed in bold.
- The page name can be directly edited in the tree view.

#### Representation of the page structure in the tree

The projects form the first level in the tree. The pages are displayed below the projects. These are displayed by default according to the page structure you have defined.

In the process all the used structure identifiers of the identifier blocks that are identified in the page structure as identifying are displayed by default in the tree view of the page navigator. By default, descriptive and unused identifiers are not displayed.

You have the possibility to influence the display of the tree structure in the page navigator in the project settings (File > Settings > Projects > "Project name" > Display > Tree structure (pages)). You can hide or display the structure identifiers of one or more identifier blocks and / or have the page type displayed additionally.

![](../Pictures/Gui/ALL/note.png)Note:

Please note that the sequence of the pages in the List view of the page navigator are by default decisive for the page output (printing, PDF export, etc.) and for the browsing through pages in the graphical editor. You have to activate the project setting Also use representation sequence for page outputs so that the sequence displayed in the tree view is also used for these different functionalities.

#### Reporting page types

The page type can additionally be selected for the display in the tree structure. By default, it is at the beginning of the properties list in the project settings. If the associated check box is activated, the pages on the uppermost level in the tree view of the page navigator are sorted according to page type. The following sequence is kept:

- Title page / cover sheet
- Table of contents
- Schematic single-line
- Schematic multi-line
- Fluid power schematic
- Overview
- Function overview (fluid power)
- Panel layout
- Graphic
- External document
- P&I diagram
- Reports (with an alphanumeric sorting format of the individual reports).

#### Display of sub-identifiers

In projects using structure identifiers, sub-identifiers can also be defined. When this is performed, the main identifier and sub-identifier are separated by a period. Sub-identifiers are always displayed after the main identifiers or the pre-defined auxiliary identifiers.

In the project settings you define whether main and sub-identifiers are displayed in one level of the tree, or whether the sub-identifiers are displayed at a lower level.

### List view

In the list view, all of the pages are displayed vertically in a customizable table format.

- The commands Open page, Copy, call up the properties window, etc., can be used in exactly the same way as in the tree view.
- You can select multiple pages.
- You can sort the sequence of displayed lines (i.e. the pages) according to any desired column, in ascending or descending order, by clicking the column headers.
- Some fields, such as the Page description, Drawing number, etc., can be directly edited in the list.

#### Display configuration

The list view always displays at least the information contained in the tree. You can define the content and sequencing of further information to be displayed in the columns. All page properties can be used. In small and medium-sized projects, you can display all page information in the list that you currently require. If the amount of information in larger projects is too large and the display is too slow, then you should only display a small amount of information in the list and open the separate page properties dialog to view the information for specific pages.

See also

[Page Navigator](pagebrowsergui_k_start.htm)

[Page Types](pagebrowsergui_k_seitentypen.htm)

[Project Management](prjmanagementgui_k_start.htm)

[Dialog Settings: Tree structure (...)](modaldialogsdb_d_einstellprjstruktur.htm)

[Specifying the Representation of the Tree Structure in the Navigators](projectstructure_h_kennzeichenausblenden.htm)