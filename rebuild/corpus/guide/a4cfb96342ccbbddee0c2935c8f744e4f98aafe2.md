# Tab Layers

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

- File > Settings > User > Interfaces > DXF / DWG export and import. Select the Layers tab.
- File > Export > Command group Project data > Project data > Command group Page > DXF / DWG. Click [...] next to the Scheme field. Select the Layers tab.

To be able to uniquely recognize a logical element on a page, the DXF / DWG file must already be set up using different layers. Using the table in this tab, assign the layers used in AutoCAD to the predefined Eplan default and project layers.

Overview of the main dialog elements:

Name:

Name of the Eplan layer from the layer management, e.g. EPLAN100. Click the arrow in the field to open the drop-down list of all Eplan layers and select the desired layer.

Description:

Associated description of the Eplan layer, also from the layer management, for example Symbol graphic.General.  
Note that the description for a standard layer cannot be changed! (Standard layers are all layers with the name EPLANxxx.)

CAD name:

The default for CAD-specific layer names is taken from the Eplan layer names and then can be edited here.

Visible / Print / Locked:

Layer properties as specified in the layer management. Changes made to a property in this tab do not affect an open project.

Popup menu:

The popup menu provides - depending on the field type (e.g. date, integer, multilingual) - the following menu items that are, depending on the situation, available for influencing the table or editing the values in the fields. You can find an overview of these popup menu items in the section [Popup menu items](userinterface_m_kontextmenu.htm).

[Add]:

Click this button in order to automatically add all of the layers in the current project to the table and edit the assignments. If layer allocations have already been defined, then these are not overwritten by this function.

![](../Pictures/Gui/ALL/note.png)Note:

Layers not contained in this list are transferred unchanged and an attempt is made to transfer all of the layer properties (line thickness, font size, etc.) too.

See also

[Dialog Settings: DXF / DWG export and import](xdxfgui_d_einstellungen.htm)

[Dialog Layer management - <Project name>](layermanager_d_ebenenverwaltung.htm)