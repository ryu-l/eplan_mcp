# Global Editing of Properties on Report Pages

The global editing feature allows you to make changes on [report pages](Glossary_o_auswertungsseiten.htm) that are immediately adopted on all [logic pages](Glossary_o_logikseiten.htm) in all views.

![](../Pictures/Gui/ALL/note.png) Notes:

- If you change the data of an object on a report page, then the row or column containing the object on the page is updated. Note that other report pages that may also contain this object data remain unchanged. You may need to also update these [reports](Glossary_o_auswertungen.htm).
- On report pages of page types Forms documentation, Plot frame documentation, Revision overview, and Symbol overview, global editing is not possible.
- Reports generated in a different project lose their reference to the original [objects](Glossary_o_objekte.htm). Global editing on such pages is therefore not possible.
- Some entries on report pages have no reference to an object. No editing dialog can be opened for such entries - a double-click then always opens the Properties - Placeholder text dialog.

Precondition:

You have opened a report page.

1. Select the desired placeholder text on the report page.
2. Select Popup menu > Properties (global).  
     
   ![](../Pictures/Gui/ALL/arrow.png) The editing dialog linked to the source object opens.
3. Make the desired changes in the respective dialog.
4. Click [OK].  
     
   ![](../Pictures/Gui/ALL/arrow.png) The changes are immediately adopted on the report page. The data of the source object is also automatically updated on all logic pages in all views.

![](../Pictures/Gui/ALL/example.png) [![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

While examining an opened device tag list, you discover that a safety fuse has the wrong DT -F25. Position the cursor over the device tag of this function and select Popup menu > Properties (global).

The dialog Properties (global): General device opens. In the Safety fuse (Device) tab, click the Full DT and change (e.g.) the device tag counter to 3. After you close the dialog by clicking [OK] the new DT will be immediately displayed in the device tag list. The device tag is also updated on all logic pages liked to this function (e.g. Schematic multi-line).

The wrong DT for the safety fuse is also shown in the project parts list. Update this page (e.g. manually). To do this, select the parts list in the page navigator and then select Utilities > Reports > Update. The parts list now shows the correct DT.

If under Options you have selected the Properties (global) menu item, then double-clicking a placeholder text also opens the respective editing dialog of the source object. If this option is not selected, then double-clicking a placeholder text opens the Properties - Placeholder text dialog.

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

You have opened the table of contents of a project and wish to change the page description of the Power supply schematic page. To do this, in the Options menu, select the Properties (global) mode. Then double-click the text to be changed in the report page. The Page properties dialog opens. After changing the text in the Page description field to Power supply station 1 click [OK]. The new page text is displayed in the table of contents and the changes are immediately adopted in the page navigator and the plot frame of the schematic page.

![](../Pictures/Gui/ALL/info.png) Tip:

You can set up EPLAN so that existing report pages are automatically updated when opened. To do this, select the user setting Update reports when opening pages (under Options > Settings > User > Display > General).

See also

[Global Editing on Report Pages](Reverseengineering_k_start.htm)

[Globally Changing the DT at Functions](devicetaggui_h_bmkaendern.htm)

[Manually Updating a Report](formgeneratorgui_h_auswaktualisieren.htm)

[Updating a Report Automatically / Not Automatically](formgeneratorgui_h_automatischaktualisieren.htm)