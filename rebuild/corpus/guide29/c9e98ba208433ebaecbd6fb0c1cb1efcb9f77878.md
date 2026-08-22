# Connection Point-specific Reports of Terminals

Connection point-specific [reports](Glossary_o_auswertungen.htm) for terminals output the terminal connection point to which terminal targets are connected. To this purpose the placeholder elements Terminal connection point internal and Terminal connection point external are available for terminal diagrams and terminal [connection diagrams](Glossary_o_anschlussplaene.htm). Amongst other things the corresponding [connection point designations](Glossary_o_anschlussbezeichnungen.htm) may be output via these.

The [form](Glossary_o_verlauf.htm) property Connection point-specific output can be used to specify that connection point-specific reports should be generated for terminals. If this property is selected, a line is generated for each connection point pair (external / internal) in terminal diagrams and terminal connection diagrams. Terminals with more than two [connection points](Glossary_o_anschluesse.htm) are automatically split across multiple rows. Connection points without targets are not output.

The terminal's connection point logic determines whether a connection point is external or internal and therefore where it will be output on the report page. By default, EPLAN considers [items](Glossary_o_bauteile.htm) below a terminal in the path as external targets and items above the terminal as internal targets. (For example, in a terminal with four connection points, one connection point may be output as internal and three as external.) In addition, terminal connection points that are not connected are output. In addition, jumpers between an internal and an external connection point are not evaluated and displayed as jumpers.

If the form property Connection point-specific output is disabled, terminals are reported in relation to targets. In target-specific reports the external and internal targets of the terminal are output. For each target, the connection point of the terminal to which the target is connected can be specified using the placeholder elements Terminal connection point internal and Terminal connection point external.

![](../Pictures/Gui/ALL/note.png)Note:

Even with the Connection point-specific output form property being deactivated, jumpers between an internal and an external connection point are not evaluated and displayed as jumpers if one of the following placeholder elements is used in the form:

- Target via connection point
- Connection via connection point
- Connection / cable via connection point.

![](../Pictures/Gui/ALL/info.png)Tip:

View > External targets can be used to display the defined external targets in the graphic editor with small arrows. This makes [target tracking](Glossary_o_zielverfolgung.htm) for terminals easier.

### Output of saddle jumpers

For terminals, only non-saddle jumper connection points are output in connection point-specific reports. The existing saddle jumpers are output as well at these connection points. Therefore, saddle jumpers can be output only if on the same side of the terminal (internal / external) at least a non-saddle jumper connection point is output as well. Saddle jumpers that connect an internal with an external connection point are not output in connection point-specific reports.

Manual saddle jumpers are placed from the last to the second-to-last connection point of the terminal. If all non-saddle jumper connection points are on the same side of the terminal (e.g., external), then at this terminal there is no internal side, and thus there is no way of outputting there an internal saddle jumper connection point. This means:

- If all non-saddle jumper connection points are "external", then the saddle jumper connection points must be set to "external" as well.
- If all non-saddle jumper connection points are "internal", then the saddle jumper connection points must be set to "internal" as well.
- If there are internal and external non-saddle jumper connection points, the saddle jumper connection points can be set to "external" or "internal" as well.

In target-specific reports, all saddle jumpers are output.

### Output of direct connection points

Terminals can have direct connection points. For this purpose the "Direct connection point" connection point type must be set in the connection point logic. Such direct connection points are now evaluated like normal terminal connection points and the connection point [designations](Glossary_o_bezeichnungen.htm) are output in connection point-specific reports (e.g. In the terminal diagram).

Exception: For [function definitions](Glossary_o_funktionsdefinitionen.htm) with rail contacts such as "PE terminal with rail contact, 2 connection points", the direct connection points (meaning the rail contacts) are not output.

See also

[Managing Terminals](terminalgui_k_verwaltung.htm)