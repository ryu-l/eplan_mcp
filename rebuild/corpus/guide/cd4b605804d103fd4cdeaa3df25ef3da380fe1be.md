# Tab Fins (NC Export Steinhauer)

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

- File > Settings > Company > Machining > NC export Steinhauer. Select the Fins tab.
- File > Export > Command group Manufacturing data > Machining > Steinhauer - ModCenter. Click [...] next to the Machine field. Select the Fins tab.

To prevent damage to the milling tool in the case of rectangular surfaces to be milled that are too big, such surfaces can be divided by fins. This creates smaller milling areas. The resulting fins are broken out during the mounting. All settings regarding automatic fin processing are specified in this tab.

![](../Pictures/Gui/ALL/note.png)Notes:

- To prevent the destruction of the outline during the approach of the milling tool, the following condition applies to outlines of small height: Fins are finished in connection with rectangles only if the smaller side is at least 20 mm long.

The following rules apply to chamfered / rounded rectangles:

- If the setting on this tab says that on the entire side length (side width or height) three fins are to be generated, and the available length is sufficient for only two fins due to the chamfer / rounding, then two fins will be fabricated.
- If the setting on this tab says that on the entire side length (side width or height) two fins are to be generated, and the available length is sufficient for only one fin due to the chamfer / rounding, then one fin will be fabricated.
- These rules are applied if the side length minus chamfer distance / fillet radius is greater than the fin width plus double the milling diameter / drill hole diameter.

Overview of the main dialog elements:

Group box Settings for chamfered and non-orthogonal rectangles

Use the default settings or change the values for the individual settings in accordance with your requirements.

Fin width:

A fin width of 1 mm is set as standard.

Generate one fin if edge length exceeds:

By default, a fin is inserted from a milling length of 100 mm.

Generate two fins if edge length exceeds:

By default, two fins are inserted from a milling length of 250 mm.

Generate three fins if edge length exceeds:

By default, three fins are inserted from a milling length of 500 mm.