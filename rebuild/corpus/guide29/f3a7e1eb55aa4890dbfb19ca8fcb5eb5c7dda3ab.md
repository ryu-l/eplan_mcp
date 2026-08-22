# Dialog Readdress PLC connection points

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have opened a project. You have selected several [PLC connection points](Glossary_o_sps_anschluesse.htm) in the graphical editor, the PLC navigator, or in the device navigator. Or you have selected one or more pages or a project in the page navigator. Project data > PLC > Address.

It is possible to re-address entire or partial areas of PLC [connection points](Glossary_o_anschluesse.htm) within a PLC controller (several PLC connection points, one or more [PLC cards](Glossary_o_sps_karten.htm)). In the process the CPU belonging to the PLC connection points is determined and the scheme assigned to the CPU is used for addressing. If no scheme is assigned to the CPU, the scheme specified in the project [settings](Glossary_o_einstellungen.htm) is used.

![](../Pictures/Gui/ALL/note.png)Notes:

- Only the PLC connection points of one CPU can be addressed respectively. If you have selected PLC connection points belonging to different CPUs, a selection dialog is displayed prior to the opening of the Reassign PLC addresses dialog, and you have to decide for a CPU.
- Only the selected connection points are re-addressed. If the connection points are selected in both the schematic and the overview page, then the new address is transferred to both placements. Otherwise the addresses in the schematic and the overview page are different.

Overview of the main dialog elements:

PLC-specific settings:

The scheme which defines the format of the [PLC addresses](Glossary_o_sps_adressen.htm) is displayed in this field. The scheme is determined on the basis of the CPU that is contained in the selection and cannot be changed here. If no scheme is assigned to the CPU, the scheme specified in the project settings is used. The configuration project, the station [ID](Glossary_o_id.htm) and the CPU to which the PLC connection points are assigned are furthermore displayed via the field.

Digital connection points:

Select this check box to address digital PLC connection points.

Digital start address:

Here you enter the address from which the addressing of the PLC digital connection points is to begin. The currently defined address format is displayed above the field as a guide.

Analog connection points:

Select this check box to address analog PLC connection points.

Analog start address:

Here you enter the address from which the addressing of the PLC analog connection points is to begin. The currently defined address format is displayed above the field as a guide.

Sorting:

In addition to the start address, you define here the order in which addresses are to be assigned. The connection points are fundamentally sorted by the DT of the card; in addition, sorting can occur by the graphical order of the placements in the schematic, by the order of channel [designations](Glossary_o_bezeichnungen.htm) or by the order of the [connection point designations](Glossary_o_anschlussbezeichnungen.htm).

- By card DT and placement (graphical): The PLC connection points are addressed per card according to their graphical order in the schematic. This option is only sensible when all connection points have been placed.
- By card DT and channel designation: The PLC connection points are addressed per card according to the order of their channel designation. This option is only sensible when the channel designations are entered.
- By card DT and connection point designation: The PLC connection points are addressed per card according to the order of their channel designation. The plug designation is taken into account and sorted in front of the connection point, i.e. the connection point "-A1-X1:2" comes before the connection point "-A1-X2:1".

Apply to entire CPU:

Select this check box in order to expand the addressing to the entire CPU.

See also

[Defining Address Formats](plcprocessorgui_h_adressenformateeinstellen.htm)

[Addressing PLC Connection Points](plcgui_k_adressierung.htm)