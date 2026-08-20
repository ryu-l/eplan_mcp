# Tab <Planning object - displayed name>

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have opened a project.

- You have generated a planning object in the pre-planning navigator, or inserted one in the graphical editor. Select the <Planning object - displayed name> tab in the Properties <...> dialog.
- You have highlighted a planning object in the pre-planning navigator or in the graphical editor. Popup menu item Properties. Select the <Planning object - displayed name> tab.

On this tab, you specify the properties for the highlighted planning object.

If the entries in the fields differ from the default values of the underlying segment template in the property dialog, these are highlighted by a [yellow background](planninggui_k_segmentvorlagen.htm#GelberHintergrund).

Overview of the main dialog elements:

Designation:

Specify the name of the planning object here. The designation entered here will be displayed in the pre-planning navigator at the planning object by default.

Full designation:

This field displays the designation of the planning object including the designations of the superior planning objects and structure segments.

Description:

Enter description text for the planning object here. This text is displayed in the pre-planning navigator together with the designation at the planning object by default.

Segment template:

This field displays the segment template which is assigned to the segment. Click [...] to open the Select segment template dialog for selecting a segment template. Only segment templates which are suitable for the segment definition of the current segment are displayed. When switching to another segment template, the property values of the new segment template are applied to the segment and are displayed in the property dialog of the segment. Manually changed values are retained.

Using ![](../Pictures/Gui/ALL/all_delete_as.png) (Delete), you can remove the reference to the segment template from the segment. The property values defined in the segment template will be deleted at the segment. Manually changed values are retained.

Technical description:

Enter here a summary of the technical details for the planning object.

Product aspect:

Provide the product aspect here. The value entered here will be displayed in the pre-planning navigator at the planning object by default.

Through the popup menu item Determine new counter you can generate a new counter for the product identifier. Any existing identifiers are retained. The counter is incremented if a planning object with the same identifier already exists on the same hierarchy level in the tree.

Through the Identifier subclasses popup menu item you open the dialog of the same name to select an identifier subclass. (The identifier subclasses are stored in the project settings under "Project name" > Devices > Numbering (online).) If you confirm your selection here, a new product aspect including a counters is generated. If required, any existing product aspect is discarded. If a planning object with the same identifier already exists in the product aspect on the same hierarchy level in the tree, the counter is incremented.

Product aspect (full):

This field displays the product aspect including the product aspects of the superior planning objects and structure segments.

---

[Group box Properties](devicetaggui_r_gruppenfeldeigenschaften.htm)

See also

[Pre-planning](planninggui_k_start.htm)