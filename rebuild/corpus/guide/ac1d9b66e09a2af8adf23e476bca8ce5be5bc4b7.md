# Tab Bus data

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have opened a project.

- You have selected a network / bus cable-connection point in the graphic editor. Popup menu item Properties. In the Properties <...> dialog, select the Bus data tab.
- You have selected a network / bus cable-connection point in the device navigator or in one of the PLC navigators. Popup menu item Properties or Properties (global). In the Properties <...> dialog, select the Bus data tab.

In this tab, you define the properties for the selected bus port that it has within a bus system.

In the Properties (global) processing mode, you edit the properties of all representations of the function jointly; in this case, the tab shows the supplement "(Device)".

Overview of the main dialog elements:

Physical network: Name:

The physical network consists of all the bus ports that are physically connected to each other. Enter the name of the physical network to which the bus port is connected. This name must be unique within the [Configuration project](#Konfigurationsprojekt). Only one bus system can exist within a physical network.

Bus system:

Select the type of bus system from the drop-down list, for example "PROFIBUS", "Ethernet", "ASI", etc.

Additional information on the selected bus system that is relevant for the behavior during the PLC data exchange is shown in the info area below this field. In the process combinations of the following entries are shown:

- Port-specific interconnection: These bus systems can be exported with port-specific interconnection.
- Physical network: These bus systems form a physical network.
- Logical network: For these bus systems the logical network that is specified in the Logical network: Name property is also exported.

![](../Pictures/Gui/ALL/note.png)Note:

Special features of the bus system "EtherCAT":

- The Physical network: Bus ID / item number property is not used for the bus system "EtherCAT". The associated check run 004037 can be suppressed by activating the property Ignore missing bus ID (ID 20412) for this bus port.
- The sequence of the bus ports is determined on the basis of the connections of the bus nodes. Therefore it is essential to configure the connections between the bus ports and activate the option Export port-specific interconnection in the dialog Export PLC data.

Special features of the bus systems "Local-Bus: Extension", "DRIVE-CLiQ", "IO link", "PortToPort" and "ET connection":

- These bus systems do not form a network.
- For these bus systems only the connection between the bus ports is exported (port-specific interconnection).
- The property Bus interface: Name (ID 20447) must be identical at all associated bus ports of a device, an empty entry is permissible as well here.
- No bus address is required. The associated check run [004037](messages_p_004037.htm) can be suppressed by activating the property Ignore missing bus ID (ID 20412) for this bus port.

Physical network: Bus ID / item number:

Enter the bus ID of the bus port here. Depending on the bus system, the value is a simple number, an IP address or a combination of letters and numbers.

![](../Pictures/Gui/ALL/note.png)Note:

You have the possibility to enter a further bus ID of the bus port in the Physical network: Bus ID / item number 2 property in the Properties of the network interface group box. The property is used for ASI devices during the PLC data exchange in the AutomationML AR APC format.

---

[Group box Properties of the network interface](devicetaggui_r_gruppenfeldeigenschaften.htm)

The following properties are available, among others, for bus ports:

- Configuration project (at PLC boxes and bus ports): If the value is empty, the configuration project of the bus port is automatically determined by the associated PLC box (main function). An entry is only required if the configuration project of the bus port is different from the configuration project of the associated PLC box.
- Configuration project (automatic, at bus ports): This property outputs the manually entered configuration project or, if it is empty, the configuration project of the associated PLC box (main function) at a bus port.
- Bus interface: Name: The bus interface name serves to group bus ports for the export of [Ethernet-based bus systems](plcgui_k_spsanschluesse.htm#I_Netzwerkanschluesse). Associated bus ports are combined into a logical unit via this name. To do this use the bus ports of the type "Network / bus cable connection point, general".  
  The bus interface name is used together with the plug designation for identifying bus ports.
- Bus interface: Main bus port: Identifies a bus port within an interface as the main bus port. This bus port represents the bus interface and bears the data relevant for the data exchange (among others Physical network: Bus ID / item number, MasterSystemId). During exporting the data are read from the main bus port and written into the PLC configuration file.  
  Exactly one main bus port must exist within an interface of one of the bus ports. This is one of the bus ports of the type "Network / bus cable connection point, general".
- Ignore missing bus ID: This setting is provided for devices in bus systems that do not require a bus ID. If this property is activated at a bus port, the missing bus ID is ignored during the execution of check run [004037](messages_p_004037.htm), and no check run message is issued for this bus port.
- Logical network: Name The logical network consists of all the bus ports within a physical network that can communicate with each other. Enter the name of the logical network to which the bus port belongs. This entry has to be unique within a physical network.   
  During the PLC data exchange for IO systems you enter the name of the IO controller for the IO system here. All PLC boxes with the same logical network name belong to one IO system. The IO system determines which station (in TIA Portal "IO device") is controlled by which IO controller. This is comparable to the specification of the CPU association: While the CPU association is PLC card-oriented, the IO system is station-oriented.  
  When the "PROFIBUS" bus system is used, the "IO system" is similar to the "DP master system", the "IO controller" is similar to the "DP master" and the "IO device" is similar to the "DP slave".
- Logical network: Bus port is master: Activate this check box when the bus port represents the master of the logical network. Within an IO system (for Ethernet-based bus systems) or a DP master system (for PROFIBUS), that bus port must always be designated that is master for the assignment.

See also

[Tabs <Function category> / <Function category> (Device)](devicetaggui_r_bmdaten.htm)