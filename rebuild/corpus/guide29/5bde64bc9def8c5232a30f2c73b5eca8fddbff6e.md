# Routing Connections (Topology)

Routing [connections](Glossary_o_verbindungen.htm) are connections with the 'Topology' representation type. When routing, these connections are generated from multi-line connections, you can, however, also define the [routing connections](Glossary_o_verlegeverbindungen.htm) manually in the Interconnect devices dialog. Routing is done in two steps: First, routing connections are generated from the multi-line connections (if multi-line connections are highlighted), and then all the routing connections that exist in the selection are routed in the [topology](Glossary_o_topologie.htm). For a multi-line connection and /or routing connection to be routed, there must be topology [functions](Glossary_o_funktionen.htm) for their sources and targets.

A routing connection has all the [properties](Glossary_o_eigenschaften.htm) that a multi-line connection also has, but it also additionally contains information about its routing track. If during a [route](Glossary_o_verlegen.htm) a connection cannot find a routing track through which it can run, a non-routed routing connection is created. Such a connection graphically takes a direct path (i.e., also diagonal) between the source and target, and is represented by default as a thin orange line.

Routing connections are copied as well if their targets are highlighted. If both targets of a routing connection are deleted, this will also delete the routing connection.

### Routing of single-line cables

Routing connections can also be generated from cables with single-line representation. The resulting routing connections are identified by the property Topology: Generated single-line ([ID](Glossary_o_id.htm) 20343). Single-line individual connections can, on the other hand, not be routed.

The multi-line representation takes precedence during routing. This means:

- If a [cable](Glossary_o_kabel.htm) has a single-line representation and a multi-line representation, the multi-line representation is used during routing.
- If a multi-line representation is added to a single-line representation, the single-line routing connection is replaced by the multi-line one.

### Protected routing for cables

If the entered length at a cable is to be retained, you can exclude the cable from routing by using the Protected routing property. If this property is activated at any representation type of a cable, the cable is not taken into consideration during routing in the topology. An entered routing track and the length remain. If the Protected routing property is activated at any connection of the cable, the complete cable is also not routed.

![](../Pictures/Gui/ALL/info.png)Tip:

The Protected routing property can, for example, be used for prefabricated cables. For prefabricated cable parts (these belong to the product subgroup "Prefabricated") the length is defined via the Length (prefabricated) property in the parts management. For a [part](Glossary_o_artikel.htm) selection this length is transferred at the cable in the project. Also activate the Protected routing property to exclude the cable from routing and thus retain the length.

If the cable has already been routed in the topology or if a length was manually entered at the cable, the length of the cable can deviate from the prefabricated length. You can find deviating cable and part data via the [007023](messages_p_007023.htm) check run.

### Reports

The following [reports](Glossary_o_auswertungen.htm) can be generated on the basis of the [routing path networks](Glossary_o_streckennetze.htm) and the routed connections:

- Topology: Routing path list: Outputs the [routing paths](Glossary_o_strecken.htm) with their data and [routing points](Glossary_o_verlegepunkte.htm), or the topology functions and their data.
- Topology: Routing path diagram: Outputs for each routing path the connections and cables that pass through it.
- Topology: Routed cables / connections: Outputs all routed cables and connections of the project.

### Settings for routing connections

When generating routing connections, the project [settings](Glossary_o_einstellungen.htm) are considered that are generally defined for routing connections in the [layout space](Glossary_o_bauraum.htm) and the topology (menu path: Options > Settings > Projects > "Project name" > Routing connections > General). These settings concern the [wire termination processing](Glossary_o_verbindungsende_behandlung.htm), the connection filter for the generation of routing path networks and the global extra length for the route.

The following special features apply to topology routing connections:

- [Tab Wire termination processing](connectionsettingsgui_r_einstellungenverbindungsende.htm)
    
  The use of dual sleeves is not evaluated.
- [Tab Connection filter](connectionsettingsgui_r_einstellungenverbindungsfilter.htm)
    
  The filter criteria defined here are available later in the project for selection at the routing paths in the property Topology: Connection filter (ID 20247).  
  The connection filter is used during routing to control which connections may be routed through which routing track (routing paths and routing points).
- [Tab Route](connectionsettingsgui_r_einstellungenverlegung.htm)
    
  For routing connections in topology, the settings made here are not evaluated.

### Function definitions of the connections

Only connections with the following [function definitions](Glossary_o_funktionsdefinitionen.htm) are routed:

- Conductor / wire
- Connection general
- Tube
- Pipe
- Non-electrical connection
- Optical fiber
- Process engineering.

### Properties of the routing connections

The following properties are entered at the connection during routing:

| Property | Meaning |
| --- | --- |
| Connection: Length | Length of the connection from the source to the target. The length is determined from all routing paths and routing points that have been passed through, including lengths from the connection point pattern (X, Y, and Z position and [additional length](Glossary_o_zusatzlaenge.htm)), connection point lengths of source and target, and a global extra length. The lengths are always rounded off to full mm. |
| Connection: Connection point length (Source / Target) | Indicates the item length of the connection that is required to connect the source or target item. It is by this value that the connection must project at the last routing point. |
| Topology: Routing track | Here, the routing paths passed through from the source to the target with DT are listed. The names are separated by a semicolon.  An empty Topology: Routing track property indicates a non-routed connection. If a route is removed, this property will be cleared again. |
| Topology: Routing track specification | The Topology: Routing track specification connection property is filled by modifying the routing track manually. Subsequently, the connection [filters](Glossary_o_filter.htm) are no longer taken into account for the routing of these connections.  The routing track specification of a connection has priority. So, for example, if a voltage is not permitted, but the routing track specification of the routing path has been entered, the routing path will be used and routed without regard for any other connection filters. |
| Wire termination processing source / target | The intended processing of wire terminations is entered for routing connections according to the settings. |
| Connection dimension source / target | During routing, the [connection dimension](Glossary_o_anschlussmass.htm) is carried over from the properties of the topology function (Connection point pattern tab) to these two properties. |

The following properties are additionally entered on cables:

| Property | Meaning |
| --- | --- |
| Length (prefabricated) | Length of the cable from the source to the target. The length is determined from all routing paths and routing points that have been passed through and from the lengths of the connections. The lengths are always rounded off to full mm. |
| Cable: Connection point length (Source / Target) | Indicates the item length of the connection that is required to connect the source or target item. It is by this value that the cable must project at the last routing point. |
| Topology: Routing track | Here, the routing paths passed through from the source to the target with DT are listed. The names are separated by a semicolon.  An empty Topology: Routing track property indicates a non-routed connection. If a route is removed, this property will be cleared again. |
| Cable / Conduit: Stripping length (Source / Target) | The [stripping length](Glossary_o_absetzlaenge.htm) is derived from the longest connector from the entry point into the device, as well as the additional length from the connection point pattern. |

See also

[Routing Paths (Topology)](cablinggui_k_start.htm)

[Routing Connections (Topology)](cablinggui_h_verlegen.htm)

[Consideration of Height Differences during Routing](cablinggui_k_teilstrecke.htm)