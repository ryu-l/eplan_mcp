# PLC Connection Points

### I/O connection points

A PLC I/O connection point belongs to a PLC card or to a channel on the card. A connection point always has a connection point designation, and often has a connection point description as well. A PLC I/O connection point is uniquely identified via the DT of its PLC box, its plug designation and its connection point designation.

Each Connection point designation may only occur once per card, but may occur several times within a PLC. If the PLC connection points are differentiated additionally through the plug designation, the connection point designations may occur several times within a card.   
Each Connection point description may only occur once per channel, but may occur several times per card. The card power supplies may also have identical connection point descriptions.

The address is not identifying for a PLC connection point and is not compulsory when planning. At a later time, the addresses can be automatically assigned by the Eplan automatic addressing function, or can be read from an assignment list.

A PLC connection point has the following properties, among others:

- Symbolic address: The symbolic address can be manually or automatically assigned.
- Function text: The function text can be entered manually, or entered automatically from the path of the schematic page if this exists and has not been entered at any of the functions. For channel symbols, the function text is adopted from the insertion point of the symbol and not the associated connection point of the input or output.
- Plug designation: The designation of the plug (for example, -X1) on which the connection point or the channel is located on the card is entered here. As with terminals, the plug designation is adopted from the left (or above). A PLC card plug does not appear as an independent object in the navigator. The plug designation is only information for the PLC connection points / channels that supports identification of an individual PLC connection point. If a PLC connection point is the target of a report, the plug designation is also output at this point (for example -A1-X1:1).
- Channel designation: The channel designation can be manually or automatically assigned. For PLC functions without an I/O connection point (power supply connection), the assignment is normally done graphically. You must only manually enter the channel designation when no graphical assignment is possible. The same channel designation within a card plug is then sufficient for recognizing the relationship.
- Data type: The data type specifies the addressing range (e.g., "BYTE" or "WORD") and is accounted for in the automatic addressing.
- Type of signal:For adjustable PLC connection points this property determines what type of connection point it is. The type of signal is also analyzed in the display of cross-references on the overview page. You can use a specific setting to display cross-references not only at the input and output connection points but also at the power supply connection points.
- Signal range: You can enter additional technical characteristics in this property, for example the signal range that a PLC connection point has. Possible entries are, for example, ranges for the voltage or the amperage: 0...10 V or 0...20 mA or +/-5 V or 4...20 mA. The property can also be stored in the function templates of the parts and is then transferred to the PLC connection points during a part selection. The property is identifiying at the device selection. It can be used for filtering during external editing and editing in a table. In addition the property in the list view of the PLC navigator can be displayed as well as selected in the dialogs in which you select PLC connection points or addresses to place them blockwise.

### Configurable PLC connection points (multi-function connection points)

Increasingly there are devices among the range of PLC devices whose PLC connection points are adjustable: PLC connection points can either be an input or an output. To display PLC cards with such connection points in Eplan you can use the function definition 'PLC connection point, multifunction'.

PLC connection points with this function definition are configurable: For these connection points the Type of signal property in the connection point logic determines what type of connection point it is. The default setting is "Digital input". If a type of signal is selected that defines an I/O connection point (i.e. "Digital input", "Digital output", "Analog input", or "Analog output"), the connection point is treated as the corresponding I/O connection point. Thus for example a "PLC connection point, multi-function" with the type of signal "Digital input" corresponds to a "PLC connection point, DI". If a type of signal is selected that does not define any I/O connection point, the connection point is treated as a power supply. Thus the configurable PLC connection points are not only defined by the function definition, but the signal type is also taken into account.

If you want to use configurable PLC connection points in your project, start by adding any PLC I/O connection points to the schematic and then, on the Symbol / function data tab in the properties dialog, select the "PLC connection point, multifunction" function definition for these connection points. Subsequently set the desired signal type in the connection point logic.

### Network / Bus cable connection points

To represent bus and network connection points in Eplan, the function definitions of the category "Network / bus cable connection point" are available. Such connection points are by default net-connecting and signal-transmitting. This allows for cross-connecting devices outside of a PLC or a bus system.

A network / bus cable connection point is uniquely identifiable via the DT of its PLC box, the combination between a bus interface name and the plug designation and its connection point designation.

Network connections of the Ethernet-based systems are compatible with each other in Eplan:

- BACnet
- CC-Link IE
- CC-Link IE Control
- CC-Link IE Field
- CC-Link IE Field Basic
- EtherCAT
- EtherCAT G
- EtherCAT P
- Ethernet
- EtherNet/IP
- Modbus-TCP
- Powerlink
- Profinet
- SERCOS III
- SSCNET III
- VARAN.

This means that it is possible to map switchable network interfaces that can, for example, be used alternatively in an Ethernet or PROFINET bus system.

In the parts management the bus system to be used is set in the function templates for the network connection points. When a part is assigned, a network connection point overrides a function template if the bus systems are identical or compatible. Function templates with the setting "Other bus systems" match any bus systems in the project.

During the import of PLC configuration files the connection points from the import file are also assigned to the connection points in the project if the bus systems are identical. If the bus systems are not compatible, new additional PLC connection points are generated during the import.

#### Automatic connections between corresponding network / bus cable connections

The following network / bus cable connection points are considered as belonging together and are automatically connected to each other through an internal connection if they have the same DT and belong to the same bus system:

- General Network / Bus cable connection points   
  For all bus systems. For Ethernet-based bus systems the connection points must additionally have the same bus interface name. The bus interface name must not be empty. Enter data only at the main bus port. The check run [004040](messages_p_004040.htm) can be used to find contradictory data.
- Switch connections   
  These connection points are used at passive devices (such as terminals, pins, passive switches, bus repeaters) and are treated like busbar connection points. This means that all connection points are connected to each other. In addition, the connection points must be assigned to the same physical network (Physical network: Name property).

The network is continued beyond these connection points. This becomes evident at the display of the network tracking.

Bus ports with empty DT are ignored during the search for associated bus ports. This accelerates the determination of the network structures if there are many bus ports with empty DT.

![](../Pictures/Gui/ALL/note.png)Note:

During the PLC data exchange in the AutomationML AR APC format bus ports within the same bus system and the same physical network (Physical network: Name property) are considered as connected with each other even if they have different DTs. This does not become clear during the net tracking. The [004104](messages_p_004104.htm) check run reports such bus ports as not connected to each other. This message can be ignored by you if you have deliberately configured the network structure this way because of its physical circumstances.

See also

[Structure of PLCs](plcgui_k_prinzip.htm)

[Editing PLC Data](plcgui_k_arbeitsweise.htm)

[Addressing PLC Connection Points](plcgui_k_adressierung.htm)

[Symbolic Addresses](plcgui_k_symbolischeadressen.htm)

[Channeling the Membership of Supply Connection Points](plcgui_k_kanalzugehoerigkeit.htm)

[Address Formats](plcprocessorgui_k_adressformate.htm)

[Assignment Lists](plcgui_k_zuordnungslisten.htm)

[Highlighting the Potentials, Signals, or Nets](potentialbrowsergui_h_potenzialverfolgung.htm)