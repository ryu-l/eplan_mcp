# Symbolic Addresses

Every PLC connection point or channel is usually assigned a symbolic address. In Eplan, these can be manually entered, automatically generated, or read from an assignment list.

In the Properties <...> dialog there are three properties for the symbolic address of PLC connection points:

- Symbolic address: The manually entered symbolic address
- Symbolic address (automatic): Displays the manual symbolic address (if it exists), otherwise the determined symbolic address
- Symbolic address (determined): The symbolic address determined through the target tracking.

If a manual symbolic address exists, this is adopted in the automatic symbolic address. Symbolic addresses imported from an assignment list are also overwritten by manual entries.

### Symbolic addresses for channels

Eplan supports the possibility to assign the same symbolic address to several [channels](plcgui_k_kanaele.htm) and to export and import such an assignment. One of the following conditions must apply for the channels so that the assignment of the symbolic address to the channels is output correctly during the export of the PLC data:

- The channels have the same symbolic address, the same PLC address, and the same data type.
- The channels have the same symbolic address and consecutive PLC addresses.

### Symbolic address within user-defined data types (UDT)

For the PLC data exchange as of AutomationML AR APC format Version 1.3.0 you have the possibility to nestle and manage the symbolic address of the PLC connection point within a user-defined data type. To this purpose you can specify the name and the associated data type of the UDT in the properties Symbolic address: UDT (name) and Symbolic address: UDT (data type). "UDT" stands for "User Defined Type". The actual structure of the UDT is only required in the PLC configuration program and only specified there. The values of both properties are monolingual texts. Entry of a decimal point is not permissible.

When using these properties the overall resulting symbolic address is a combination of the values of the properties Symbolic address: UDT (name) und Symbolic address of a PLC connection point, for example "<Symbolic address: UDT (name)><Symbolic address>". This combination of the values of both symbolic addresses must be unique within a CPU for a PLC connection point.

### Automatic assignment of symbolic addresses

In the PLC-specific settings you specify whether symbolic addresses are to be assigned automatically. To this purpose the Generate symbolic addresses automatically using check box has to be activated in the Format of symbolic address tab.

During automatic assignment, the so-called target tracking searches for the sensor (input) or actuator (output) connected to a PLC connection point and transfers in the identifying DT into the Symbolic address (determined) property.

If you use a project structure with identifier blocks, then you can replace the prefixes when formatting or suppress the display of particular identifier blocks (for example e"Function designation" or "Location designation"). It is also possible to include the connection point designation in the symbolic address.

Eplan recognizes a sensor or actuator from the "Signal type" entry in the connection point logic of the respective function. Information from the connection point logic is also used to decide at which connection point the search for a sensor / actuator is to be continued. If no sensor / actuator is found, then the DT of the last connected function found before the search was abandoned is entered.

There are four possible reasons why a connection point found during the target search may not be the desired one:

- The search begins at an input (i.e., looking for a sensor) and ends at an actuator connection point.
- The search begins at an output (i.e., looking for an actuator) and ends at a sensor connection point.
- The search ends at an undefined connection point.
- The search ends at a source connection point (entry for "Source / Target" in the connection point logic).

In the first case, Eplan finds (e.g.) an actuator where the potential is not continued because the actuator is a consumer.

In the second case (e.g.) a sensor is found that is a change-over contact or a three conductor initiator. The search must now proceed in two directions. For this reason, in addition to the Type of signal property with the "Sensor" or "Actuator" settings, the connection point logic also contains the Target tracking (PLC) to property, defining which connection point should be used for continuing the search.

If the subsequent search direction is not defined, then the component where the search can no longer continue becomes the target.

I/O connection points with the representation type "Overview" have no connected connections. Target tracking is therefore not possible. These PLC connection points apply the determined symbolic address from the associated multi-line or single-line PLC connection point.

![](../Pictures/Gui/ALL/note.png)Notes:

- The Symbolic address (determined) property displayed in the symbolic address can only be determined correctly if the connections are up-to-date. If necessary, recreate the connections.
- At some PLC control systems special characters are not allowed in the symbolic address. So that the DT can also be used as an automatically entered (determined) symbolic address in this case, you can replace the preceding sign used in the DT by a different character in the PLC-specific settings (in the Format of symbolic address tab).

### Further settings for the determined symbolic address

Using the Use address if search for symbolic address is unsuccessful setting in the project settings (File > Settings > Projects > "Project name" > Devices > PLC) you specify that, instead of the DT, the address is copied into the determined symbolic address when no sensor or actuator is found or the I/O connection point is not connected.

If the property Without sensor / actuator search for symbolic address is activated on an I/O connection point, the program behaves as if no sensor or actuator will be found. In this case, the address will be used as long as it has been stored in the project settings.

### Import from assignment list

When importing an assignment list, the symbolic addresses contained in the list are assigned to the PLC connection points of the selected CPU â depending on the settings.

When exporting an assignment list, the symbolic addresses and the connected target can be output separately.

### Display of the state of PLC cards

There are PLC cards that can display states. This way states such as the operating status, error statuses etc. can be signaled, for example, through built-in LEDs. You can predefine such states as free symbolic addresses without assignment to a channel or PLC connection point in the assignment list. The free symbolic addresses are exported and imported during the PLC data exchange. After an import you can use the free symbolic addresses in Eplan.

If you want to later display the free symbolic addresses and the associated function texts in the schematic you must place a symbol. The function definition "PLC connection point, internal, general" is available to this purpose. A symbol without graphic is assigned to this function definition by default. Since the corresponding LEDs are firmly integrated in the PLC card, no connections have to be drawn in the schematic.

See also

[Importing Assignment Lists](plcgui_h_importzuli.htm)

[PLC](plcgui_k_start.htm)