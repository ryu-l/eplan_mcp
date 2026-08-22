# Dialog Connection point logic

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have opened a project. You have selected a function in the graphical editor or in a navigator. Edit > Properties. In the Properties <...> dialog, select the Symbol / function data tab and click [Logic].

In this dialog, you can edit the logic model of the function, that is, the [properties](Glossary_o_eigenschaften.htm) of the [connection points](Glossary_o_anschluesse.htm).

Overview of the main dialog elements:

In the table, a column is shown for each connection point of the Function. If the entries in the fields differ from the default values of the underlying function definition, these are highlighted by a yellow background.

![](../Pictures/Gui/ALL/note.png)Note:

A transfer of logic information such as potential transfer and [target tracking](Glossary_o_zielverfolgung.htm) to other [functions](Glossary_o_funktionen.htm) at the same DT is possible at Device connection points, PLC connection points and Distributed terminals. This applies to the properties Transfer potential to, Consumer / source to and Target tracking (PLC) to. At [Distributed terminals](terminalgui_k_verteiltedarstellungklemmen.htm) a transfer within the same terminal function is possible (at multi-level terminals also within the same level).

For such a connection point reference you enter the connection point designation of the target function (of the other device connection point, PLC connection point or terminal connection point) at the starting function in the field of the respective properties. When entering this connection point reference observe the following points for the syntax:

| Connection point designation of the target function | Input connection point reference | Example  (starting function, 1 connection point) | Example\*  (starting function, 2 connection points) |
| With digits | in "" | "4" | 2,"4" |
| With characters | Without "" | B | 2,B |
| Target function with differing plug designation (for example X2) | With colon | "X2:2" | 2,"X2:2" |
| Starting function with, target function without differing plug designation | With colon (without plug designation) | ":2" | 2,":2" |

\*At a device / PLC connection point with several connection points one connection point number, which is used for the internal transfer to another function connection point, is specified by default in the connection point logic. The connection point reference for the target function has to be specified for this connection point number (in the example 2).

The check run 007027 allows incorrect entries for the connection point references in the connection point logic.

Since terminals have no plug [designations](Glossary_o_bezeichnungen.htm), an entry at [distributed terminals](Glossary_o_teilklemmen.htm) such as "X2:2" is evaluated like a simple connection point designation.

Connection point type:

Select the connection point type from the drop-down list; you have the following options:

- Undefined: The connection point can connect to any number of other connection points.
- Conductor / wire: The connection is either a conductor in a [cable](Glossary_o_kabel.htm) (then the check box Cable connection point must be selected) or a single connection (wire).
- Jumper: The connection is realized by a jumper, e.g., power jumpers for INTERBUS Inline or terminal jumpers. (Connections with the connection point type 'Conductor / wire' can also be jumpers if the Jumper property is assigned via a connection definition point.)
- Direct connection point: Direct connection between [items](Glossary_o_bauteile.htm), e.g. if a PLC card is plugged into the [rack](Glossary_o_baugruppentraeger.htm) or a fuse on a rail or the connection of a male and female pin.
- Optical fiber: The connection can be [part](Glossary_o_artikel.htm) of a hybrid cable. In [reports](Glossary_o_auswertungen.htm), you can filter according to this type of connection point.
- Wireless connection: In reports, you can filter according to this type of connection point.
- Non-electrical gen.: The connection point can interconnect with any non-electrical connection points (e.g. pipes, tubes, optical fibers, etc.).
- Functional connection point (software): Functional connection points serve to represent the logic of [PLC configuration programs](Glossary_o_sps_konfigurationsprogramme.htm) and are not output in reports.
- Fluid power: The project [settings](Glossary_o_einstellungen.htm) are used to determine to whether this is a tube or a pipe at the fluid connection.
- Internal: Connection internal to items.
- Process engineering: Process engineering connection.
- Saddle jumper: A connection as a saddle jumper to install terminals with saddle jumper connection points.

Cable connection point:

Select the check box if the connection is in a cable. This setting is taken into account when automatically generating cables.

Pressure / control port:

For fluid technologies. Select an entry from the drop-down list. The available options include "Undefined", "Pressure line", "Control line", "Drain line", "Process medium", "Heating and [cooling](Glossary_o_kuehlung.htm) medium", "Reservoir line", or "Working line".

Transfer potential to:

Here (via the connection point number), specify the other connection points to which the potential should be transferred.

Potential type:

Select the potential type from the drop-down list. The available options include "Undefined", "L", "N", "PE", "PEN", "+", "M", "-", and "SH".

Consumer / source to:

Here (via the connection point number), specify the other connection point to which a consumer or generator (source) is internally connected.

Type of signal:

Select the signal type for the connection point from the drop-down list. Available options include "Undefined", "Sensor", "Actuator", "Power supply", "Device power supply", "Source", "Digital input", "Digital output", "Analog input", "Analog output", "Bus source", "Bus input", "Bus output", "Pressure connection point", and "Suction port".

Target tracking (PLC) to:

Here (via the connection point number), specify the other connection points to which target tracking should be transferred. The sequence for the target tracking specified here, is considered for the [automatic assignment of the symbolic address](plcgui_k_symbolischeadressen.htm#I_AutomatischeVergabe).

Number of targets:

Here, specify the number of possible targets / [connections](Glossary_o_verbindungen.htm), which the connection point may have.

Number of saddle jumpers:

For terminals, provide the number of possible saddle jumpers.

Internal / External:

Determine here whether the connection point should be interpreted as internal or external. This setting also has an influence on the connection of [devices](Glossary_o_betriebsmittel.htm) (and therefore determines how they are displayed within reports such as the device connection diagram).

Intrinsic safety possible:

Select this check box to allow the connection point to be intrinsically safe. If it is later specified in the function that it is internally safe, then all connection points will be intrinsically safe for which this check box is selected.

Allow same connection point designations:

If this check box is selected, then same [connection point designations](Glossary_o_anschlussbezeichnungen.htm) are allowed for the corresponding connection point within a device. This means that if a device includes several functions, these functions can have the same connection point designation.

If the check box is deselected, the corresponding connection point designations within a device must be unique.

![](../Pictures/Gui/ALL/note.png)Note:

If you place the functions in several [representation types](Glossary_o_darstellungsarten.htm), you should not activate this setting and define each function uniquely. Otherwise there may be problems in global editing.

Symbol connection point:

Here, you can assign the connection points of the function to the connection points of the symbol. Normally, connection point "1" of the function is allocated to connection point "1" of the symbol etc. You can change this allocation by using the drop-down list.

Popup menu:

The popup menu provides - depending on the field type (e.g. date, integer, multilingual) - the following menu items that are, depending on the situation, available for influencing the table or editing the values in the fields. You can find an overview of these popup menu items in the section [Popup menu items](userinterface_m_kontextmenu.htm).

In addition, the following dialog-specific popup menu items are available:

| Menu item | Meaning |
| --- | --- |
| Go to default | Restores the values in the selected fields to the default. |

See also

[Connection Point Designations and Descriptions](fctdeflibdataexchangegui_k_anschluss.htm)

[Editing Connection Point Logic](xfctdefbrowsergui_h_anschlussdatenbearbeiten.htm)

[Dialog Function definitions](xfctdefbrowsergui_d_funktionsdefinitionen.htm)