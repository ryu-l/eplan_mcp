# Numbering with the Data from PLC Connection Points

When numbering with PLC data, only those [devices](Glossary_o_betriebsmittel.htm) are numbered whose main function is included in the range of numbering. The matching [auxiliary functions](Glossary_o_nebenfunktionen.htm) are always also numbered.

Functions numbered with data from a PLC connection point are flagged and can optionally be excluded from normal DT numbering, terminal numbering, etc.

Devices connected to [PLC connection points](Glossary_o_sps_anschluesse.htm) can accept components of the PLC address into the DT:

- On a PLC output, the DT of a function is changed if it is a main function and the corresponding connection point is an actuator.
- On a PLC input, the DT of a function is changed if it is a main function and the corresponding connection point is a sensor.
- For terminals and [pins](Glossary_o_steckerkontakte.htm), not the DT but the terminal or pin designation is modified. You specify separate format [settings](Glossary_o_einstellungen.htm) for the numbering.
- PLC [connection points](Glossary_o_anschluesse.htm) and [PLC boxes](Glossary_o_sps_kaesten.htm) are not numbered. Nested components, as well as graphical and external components, are also not numbered.

### Numbering on terminals or pins connected to a PLC

Terminals or pins between a PLC connection point and the corresponding sensor or actuator can be designated with the address or connection point designation of the PLC connection point. In this way, you can [create](Glossary_o_erstellen.htm) [designations](Glossary_o_bezeichnungen.htm) corresponding to the [GOST standard](Glossary_o_gost_norm.htm).

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

For a terminal connected to input E10.4, depending on settings, the following [terminal designations](Glossary_o_klemmenbezeichnungen.htm) are possible:

E10.4  
X1:E10.4  
X1:10.4  
X1:104

### Break the PLC address into layers

In the settings for [numbering formats](Glossary_o_nummerierungsformate.htm), you can access individual components of the PLC address. The address is broken down into different [levels](Glossary_o_etagen.htm).

| Property | Contents |
| --- | --- |
| 1st level of address | From right to left up to the first [separator](Glossary_o_trennzeichen.htm) (bit). |
| 2nd level of address | From right to left up to the second separator (byte). |
| 3rd level of address | From right to left up to the third separator (PLC card / slot). |
| 4th level of address | From right to left up to the fourth separator (device / network node). |
| 5th level of address | From right to left up to the fifth separator (network strand). |
| Prefix | From left to right, the letters until the first separator or the first digit. All characters are interpreted as separators which are not letters or digits (e.g. %). |

The numbering format can be composed of different components of the PLC address, like "Entire PLC address", "Byte", "Bit", "Separator", or "Prefix".

See also

[Numbering on Devices Connected to PLC](offlinenumerationplcgui_k_start.htm)

[Determining the Format and Range for Numbering](offlinenumerationplcgui_h_formatfestlegen.htm)

[Numbering the Devices Connected to PLC](offlinenumerationplcgui_h_bmnummerieren.htm)