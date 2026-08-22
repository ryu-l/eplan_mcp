# 2D Panel Layout: Basics

Mounting panels can be drawn in portrait or landscape format. They are allocated a device tag that defines the basic project structure for the normal items. The mounting panel is represented in the graphical editor by a special black box.

When equipping the mounting panel with several selected parts you can define the orientation of the part references to be placed, which then affects how the part references are placed in respect to each other. The orientation of the labeling of part placements can also be defined by using the angular version of symbol placement, which can then be subsequently changed in the placement properties for a placed part. It should be noted that part placements can only occur on the mounting panel; if they are outside of the mounting panel, then an appropriate message is displayed.

The dimensioning for width, height, depth, and mounting clearance are part placement properties and are stored in the parts database or in the part macro. You can define how this data is adopted by using a setting in the dialog Settings: 2D panel layout.

The Function has the '...' representation type properties allow filters to be set that reduce the size of the display. If a part placement is filtered using this type of property, then the program searches for a function with the desired representation type assigned to the part. By setting a filter where these properties are checked for the value "No" (i.e. the check box is not selected), then the dialog only displays functions / parts that exist only on the mounting panel.

![](../Pictures/Gui/ALL/note.png)Note:

Please note that the 2D panel layout navigator (Dialog 2D panel layout - <Project name>) only allows you to filter by part reference data, and not by parts data. For example, if you filter by the Mounting surface property (ID 22022), then the filter accesses the corresponding property of the part reference data (ID 20918). However, this property can differ from the part property (ID 22022), since the mounting surface of the master data part and the part stored does not have to be identical to the mounting surface of the part reference.

In addition to this, you can define whether a Page legend is to be generated for every mounting panel, and if so, then what form is to be used for this. If the legend is not activated, then the full DT for the part symbol is written. Otherwise, all part placements receive a sequential number and the associated legend can be freely placed next to the mounting panel.

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

![](../Pictures/Visualisation/ALL/panellayoutgui_grundlagen_av.png)

The 2D panel layout - <Project name> dialog displays all the part references that exist in the project. Using the View popup menu item, the Tree tab allows you to choose between the default configurations for the displays, each of which displays the following data (if available):

- Project structure: Display of part status, identifier blocks (function designation, location designation, etc.), device tag, and part number.
- Project structure with identifiers: Display of mounting panel name (including structure identifier) or part status, identifier blocks (function designation, location designation etc.), device tag and part number.

The part status can have the following values:

| Part status | Explanation |
| --- | --- |
| All parts | This tree structure level always shows all parts. An icon (green check mark) at the part number visualizes if this part is placed yet. In the next-higher level, a check mark at the device tag indicates that all parts of the device are placed. |
| Incorrectly placed | An item that has already been placed is moved outside the mounting panel, and the panel layout navigator then updates (when you press [F5], for example).  This status cannot occur during "normal" placement as you are not permitted to place items in this way. In the event of an error, the placement is rejected. |

The devices are sorted according to the structure identifiers of the device structure. Devices that have not been sorted into a defined project structure by means of structure identifiers are sorted into the tree structure level "Without structure identifier". This tree structure level is displayed only in projects with an identifier structure (e.g., IEC identifier structure); that is, it is not displayed in sequentially numbered projects. Devices without a DT are sorted into the "Without DT" tree structure level below the tree structure level "Without structure identifier". This behavior is similar to the display of devices without DT in other navigator dialogs.

In the List tab, the data is not hierarchically structured, and the range of the display can be defined by using the popup menu Configure representation menu items.

See also

[2D Panel Layout](panellayoutgui_k_start.htm)

[Dialog Settings: 2D panel layout](panellayoutgui_d_schaltschrankaufbaueinstellungen.htm)