# Black Boxes

The black box is a popular method of representing [devices](Glossary_o_betriebsmittel.htm) for which no symbol exists in a symbol library prescribed by the end customer. Black boxes are used in various different ways:

- For devices / [assemblies](Glossary_o_baugruppen.htm) that are not in the symbol library
- For devices / assemblies that are not complete in the symbol library, e.g., with missing PE / PEN [connection points](Glossary_o_anschluesse.htm)
- For representing PLC assemblies
- For representing complex devices, e.g., frequency converters; these devices are drawn over several schematic pages and cross-referenced
- For representing several [symbols](Glossary_o_symbole.htm) under a single device tag, e.g., a motor with brakes
- For representing spare [cable connections](Glossary_o_kabelverbindungen.htm) in cables (without a black box, the "Cable connection without [cable](Glossary_o_kabel.htm)" error message is generated)
- For nesting several device tags, e.g., for a device with several terminal strips:  
  Device: -A1, terminal strips: -X1 and -X2  
  The nesting allocates the device tags -A1-X1 and -A1-X2 to the terminal strips.
- For allocating device tags to terminals, since the terminal DT can't be moved (because otherwise the connection point designation would also be moved), for example required due to a lack of space on the page
- For special protection devices that cannot be represented using the normal symbols, but which must also display a [contact image](Glossary_o_kontaktspiegel.htm).

See also

[Black Boxes: Fields of Application](blackbox_k_einsatzmoeglichkeiten.htm)

[Black Boxes: Nesting Basics](blackbox_k_schachteln.htm)

[Inserting Black Boxes](blackbox_h_kasteneinfuegen.htm)