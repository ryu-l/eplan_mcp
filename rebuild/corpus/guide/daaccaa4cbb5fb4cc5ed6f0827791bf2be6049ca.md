# Function-related Reports

In contrast to [Report overviews](formgeneratorgui_k_auswertungsuebersicht.htm), function-related reports have a device in the header as standard, e.g., a terminal strip. The associated functions are in the data area, e.g., the terminals of a terminal strip.

Function-related reports can only occur once in the project.

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

A terminal diagram of terminal strip X1 may occur only once in the project.

The following tables show function-related reports.

#### [ClosedSymbols](javascript:void(0);)

|  |  |
| --- | --- |
| Report type | Symbol overview |
| Reporting behavior | Function-related report |
| Form | [Symbol overview (\*. f25)](placeholder_o_main.htm#1820141) |
| Description | Symbols from symbol libraries stored in the project.  (See also: [Documenting Symbol Libraries](symboleditorgui_h_symbolbibliothekendokumentieren.htm)) |

#### [ClosedTerminals and parts](javascript:void(0);)

|  |  |
| --- | --- |
| Report type | Terminal line-up diagram |
| Reporting behavior | Function-related report |
| Form | [Terminal line-up diagram (\*. f12)](placeholder_o_main.htm#1220000) |
| Description | Shows terminals in list form. A terminal line-up diagram for each terminal strip. |

#### [ClosedEnclosure information](javascript:void(0);)

|  |  |
| --- | --- |
| Report type | Enclosure legend |
| Reporting behavior | Function-related report |
| Form | [Enclosure legend (\*. f18)](placeholder_o_main.htm#2900190) |
| Description | Project data of part placements. Shows the relationship between the parts in the schematics, the part position in the bill of materials, and the graphical object or part placement on the mounting panel. All part placements are allocated a sequential number. The enclosure legends can be created as report pages or inserted as "Free placements" into a page of type "Panel layout".  (See also: [Generating Enclosure Legends](panellayoutgui_h_legendenanlegen.htm)) |

#### [ClosedDrill hole information](javascript:void(0);)

|  |  |
| --- | --- |
| Report type | Cut-out legend |
| Reporting behavior | Function-related report |
| Form | [Cut-out legend (\*. f47)](placeholder_o_main.htm#5800190) |
| Description | Drill holes of the 2D drilling view. Lists the drill holes with their X-, Y-coordinates, the drill type, the diameter of the drill hole as well as the item description. |

#### [ClosedPLC connection points](javascript:void(0);)

|  |  |
| --- | --- |
| Report type | PLC diagram |
| Reporting behavior | Function-related report |
| Form | [PLC diagram (\*. f19)](placeholder_o_main.htm#2420029) |
| Description | Lists the PLC connection points of the PLC cards, which are useful for reporting. A diagram for each PLC card. |

#### [ClosedLines / conduits](javascript:void(0);)

|  |  |
| --- | --- |
| Report type | Conduit / line plan |
| Reporting behavior | Function-related report |
| Form | [Conduit / line plan (\*. f46)](placeholder_o_main.htm#5700117) |
| Description | Properties of conduit, piping and hose line definitions. |

### Connection diagrams

The following tables show report types for function-related connection diagrams that output the directly connected targets up to the next device.

#### [ClosedCables](javascript:void(0);)

|  |  |
| --- | --- |
| Report type | Cable diagram |
| Reporting behavior | Function-related report |
| Form | [Cable diagram (\*. f09)](placeholder_o_main.htm#1120085) |
| Description | Cable properties. Lists the cable connections of the cables. |

#### [ClosedTerminals](javascript:void(0);)

|  |  |
| --- | --- |
| Report type | Terminal diagram |
| Reporting behavior | Function-related report |
| Form | [Terminal diagram (\*. f13)](placeholder_o_main.htm#920025) |
| Description | Lists the terminals of the terminal strips. A terminal diagram for each terminal strip. Structure and connection point / wiring information. |

#### [ClosedPlugs](javascript:void(0);)

|  |  |
| --- | --- |
| Report type | Plug diagram |
| Reporting behavior | Function-related report |
| Form | [Plug diagram (\*. f22)](placeholder_o_main.htm#2820025) |
| Description | Lists the pins. A plug diagram for each plug. Structure and connection point / wiring information. |

#### [ClosedTopology: Routing paths](javascript:void(0);)

|  |  |
| --- | --- |
| Report type | Routing path diagram |
| Reporting behavior | Function-related report |
| Form | [Topology: Routing path diagram (\*.f35)](placeholder_o_main.htm#4520031) |
| Description | Outputs for each routing path the connections and cables that pass through it. |

#### [ClosedPre-planning](javascript:void(0);)

Structure segment plans belong to the reports in pre-planning.

|  |  |
| --- | --- |
| Report type | Pre-planning: Structure segment plan |
| Reporting behavior | Report overview |
| Form | [Pre-planning: Structure segment plan (\*.f39)](placeholder_o_main.htm#4900117) |
| Description | Outputs the properties of the structure segment per segment as well as the directly subordinate segments. |

Planning object plans belong to the reports in pre-planning.

|  |  |
| --- | --- |
| Report type | Pre-planning: Planning object plan |
| Reporting behavior | Report overview |
| Form | [Pre-planning: Planning object plans (\*.f41)](placeholder_o_main.htm#5120072) |
| Description | Outputs per planning object the properties of the planning object, the data entered at the planning object as well as the directly subordinate segments. |

Segment template plans belong to the reports in pre-planning.

|  |  |
| --- | --- |
| Report type | Pre-planning: Segment template plan |
| Reporting behavior | Report overview |
| Form | [Pre-planning: Segment template plan (\*.f43)](placeholder_o_main.htm#5320072) |
| Description | Outputs the data per segment template which are entered at the segment template. |

### Other connection diagrams

The following table shows report types for function-related connection diagrams, following the targets of connection points over multiple devices.

#### [ClosedConnection points by device](javascript:void(0);)

|  |  |
| --- | --- |
| Report type | Device connection diagram |
| Reporting behavior | Function-related report |
| Form | [Device connection diagram (\*. f05)](placeholder_o_main.htm#2520025) |
| Description | Lists the connection points of devices. Sorting by device. |

#### [ClosedConnection points by cable](javascript:void(0);)

|  |  |
| --- | --- |
| Report type | Cable-connection diagram |
| Reporting behavior | Function-related report |
| Form | [Cable connection diagram (\*. f07)](placeholder_o_main.htm#2610005) |
| Description | Lists the cable connections of the cables (as for a cable diagram, but with other forms and over several layers). Sorting by cable. |

#### [ClosedConnection points by terminal strip and terminal](javascript:void(0);)

|  |  |
| --- | --- |
| Report type | Terminal-connection diagram |
| Reporting behavior | Function-related report |
| Form | [Terminal-connection diagram (\*. f11)](placeholder_o_main.htm#1020025) |
| Description | Lists the terminals on the terminal strips (as with a terminal diagram, but with other forms and over several layers). Sorting corresponds to the order of the terminals on the terminal strip. Connected targets are displayed. |

#### [ClosedConnection points by plug and pin](javascript:void(0);)

|  |  |
| --- | --- |
| Report type | Pin-connection diagram |
| Reporting behavior | Function-related report |
| Form | [Pin-connection diagram (\*. f21)](placeholder_o_main.htm#2720025) |
| Description | Lists the pins (as in a plug diagram, but with other forms and over multiple layers). Sorting corresponds to the order of pins in plugs. Connected targets are displayed. |

See also

[Reports](formgeneratorgui_k_start.htm)

[Overview reports](formgeneratorgui_k_auswertungsuebersicht.htm)

[Creating a Function-related Report without a Template](formgeneratorgui_h_funkbezogauswerterzeugen.htm)

[Creating a Report Overview without a Template](formgeneratorgui_h_auswerterzeugen.htm)