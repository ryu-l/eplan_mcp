# Generating Cable Assignment Diagrams

[Cable assignment diagrams](cablegui_k_kabeldarstellungsplan.htm) are generated in combination with a [form](Glossary_o_verlauf.htm) for the summarized parts list. [Forms for cable assignment diagrams](formeditorgui_k_kdpformular.htm) make it possible to output data for the [cable](Glossary_o_kabel.htm) diagram and data for the summarized parts list. A cable assignment diagram is generated for each cable type. The cable assignment diagram of a cable type thus contains all cables of that cable type. Every cable to be included in the report must be assigned a form.

Precondition:

You have access to the cable assignment diagram form \*.f08 and a summarized parts list form, \*.f02.

### Place insertion point of next form

In order to specify [forms](Glossary_o_formulare.htm) for the [Next form](formeditorgui_k_folgeformulare.htm) you have to place an insertion point for the next form in that form.

1. Select the Utilities > Master data > Form > Open menu [items](Glossary_o_bauteile.htm).
2. Select the Cable assignment diagram (\*.f08) entry from the File type field, select the form and click [Open].
3. Select the menu items Insert > Insertion point of next form.
4. In the Insertion point of next form dialog, select the "Summarized parts list" entry from the Report type field.
5. To output the summarized parts list on a new reporting page, select the New page check box.
6. To output the summarized parts list on the reporting page of the cable assignment diagram, deselect the New page check box.
7. Click [OK].
8. Place the insertion point of the next form on the form page.
9. Close the form.

### Specify the next form

1. Select the Utilities > Reports > Generate menu items.
2. In the Reports dialog select [Settings] > Output to pages.
3. Click in the "Cable assignment diagram" reporting type line in the column Next form and then click "Browse".
4. Select the Summarized parts list (\*.f02) file type from the subsequent dialog, and select a form.
5. Confirm your entries.

### Assign form to all cables of one cable type

1. Select the Project data > Cables > Navigator menu items.
2. Select the entry "Main function" in the Filter field of the List tab.
3. Select the Configure representation popup menu item, activate the Cable / Conduit: Type property and click [OK].
4. Select all [cable definitions](Glossary_o_kabeldefinitionen.htm) of one cable type in the List tab.
5. Select the Properties popup menu item.
6. Select the Cable tab.
7. In the Properties group box click ![](../Pictures/Gui/ALL/all_new_as.png) (New).
8. Select the Cable assignment diagram form property and click [OK].
9. Click within the Cable assignment diagram form property line in the Value column and then click "Browse".
10. In the next dialog select a form for the cable assignment diagram.
11. Confirm your entries.
12. Assign forms to the other [cable types](Glossary_o_kabeltypen.htm) in the same way.

### Generate reports

1. Select the Utilities > Reports > Generate menu items.
2. Select the Reports tab. Click ![](../Pictures/Gui/ALL/all_new_as.png) (New).
3. In the Select report type field of the subsequent dialog, select the "Cable assignment diagram" entry. Click [OK].
4. Click [OK] in the Settings - <Report type> dialog.
5. To specify the starting page, in the Cable assignment diagram dialog select the structure identifier for the page structure or enter a new structure identifier.
6. Click [OK].  
     
   ![](../Pictures/Gui/ALL/arrow.png) All cables for which the same cable assignment diagram form has been entered, are output together in one report block. If you have used a separate cable assignment diagram form for each cable type, a report block is generated for each cable type. The report block contains reporting pages for the cable assignment diagram and the summarized parts list. A possible sorting is only taken into consideration within a report block.

See also

[Report Blocks](formgeneratorgui_k_auswertungsbloecke.htm)

[Manually Updating a Report](formgeneratorgui_h_auswaktualisieren.htm)

[Deleting Report Pages](formgeneratorgui_h_auswertungloeschen.htm)

[Freezing Report Pages](formgeneratorgui_h_auswerteinfrieren.htm)