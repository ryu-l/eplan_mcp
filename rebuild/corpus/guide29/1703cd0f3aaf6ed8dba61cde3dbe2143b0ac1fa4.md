# Representing Cables using Bundle Connection Points

EPLAN allows a clearer view of [cable](Glossary_o_kabel.htm) display by using [bundle](Glossary_o_buendel.htm) [connection points](Glossary_o_anschluesse.htm). Just before the cable source, the [cable connections](Glossary_o_kabelverbindungen.htm) enter a cable bundle via [bundle connection point symbols](Glossary_o_stranganschlusssymbole.htm).

Near to the cable target, the bundle is split again using bundle connection point [symbols](Glossary_o_symbole.htm) and the individual cable [connections](Glossary_o_verbindungen.htm) continue in split (multi-line) [form](Glossary_o_verlauf.htm). The following section provides a concrete example of how you can [create](Glossary_o_erstellen.htm) this type of bundled cable display. In this example, a terminal strip is connected to a motor via a bundle.

Preconditions:

- You have opened a project.
- The project contains a new multi-line schematic page.
- The schematic page is opened in the graphical editor.

### [ClosedInserting the cable source and drawing the entry bundle connection points](javascript:void(0);)

In the first step you insert the cable source, which consists of a terminal strip with four simple terminals in a row. You then draw the bundle connection points, which feed into the cable bundle from the terminal strip.

1. Use the Symbol selection to insert a terminal strip into the schematic page and position it somewhere in the upper area of the schematic page.
2. Designate the terminal strip with "-X1" and the terminals one after another with "1", "2", "3" and "PE".  
     
   ![](../Pictures/Visualisation/ALL/singlepole_kabelstrangerstellen1_av.png)
3. Select the menu [items](Glossary_o_bauteile.htm) Insert > Bundle connection point > Angle.  
     
   ![](../Pictures/Gui/ALL/arrow.png) A bundle connection point of type "Angle" now hangs on the cursor.
4. Press and hold the [Ctrl] key.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The desired angle variation can now be set by rotating the mouse.
5. Rotate the mouse so that the thin connection is on top and the thick connection (bundle connection point) points to the right.
6. Release the [Ctrl] key and move the angle towards terminal 1 so that an autoconnect line joins with the terminal.
7. Click the left mouse button.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The Properties <...> dialog opens.
8. Select the Bundle connection point tab and enter "1" in the Bundle connection point designation field and, if desired, enter a Bundle connection point description.
9. If necessary, select the Display tab to define the display [settings](Glossary_o_einstellungen.htm) for the bundle connection point.
10. Click [OK].  
      
    ![](../Pictures/Gui/ALL/arrow.png) The Properties <...> dialog is closed. The angle is inserted into the schematic below terminal 1.  
      
    ![](../Pictures/Visualisation/ALL/singlepole_kabelstrangerstellen2_av.png)
11. Repeat this process for another bundle connection point of type "Angle" and insert it at the same height below the PE / PEN terminal so that the thin connection points upwards and the thick connection points to the left.
12. Assign "4" as the Bundle connection point designation.  
      
    ![](../Pictures/Gui/ALL/arrow.png) The angle makes an autoconnect line with the PE / PEN terminal. In addition to this, the thick connection points of the angles combine into a bundle.  
      
    ![](../Pictures/Visualisation/ALL/singlepole_kabelstrangerstellen3_av.png)
13. Now select the menu items Insert > Bundle connection point > T-node.
14. Rotate the T-node so that the thin connection points upwards and the thick connections points downwards.
15. Insert it below terminal 2 and enter "2" as the Bundle connection point designation.
16. Insert another T-node below terminal 3 in the same manner and designate it with "3".  
      
    ![](../Pictures/Gui/ALL/arrow.png) The following schematic is displayed:  
      
    ![](../Pictures/Visualisation/ALL/singlepole_kabelstrangerstellen4_av.png)

### [ClosedInserting the cable target and drawing the exit bundle connection points.](javascript:void(0);)

In the second step you insert the cable target, which consists of a three-phase motor with four connection points (including PE / PEN). Then you draw the bundle connection points that exit the bundle and lead to the motor.

1. Use the Symbol selection to insert a motor with PE / PEN and four connection points (name "M3", symbol number "62") into the schematic and position it a reasonable distance below the already drawn terminal strip.
2. Enter "-M1" as the device tag.
3. Add a "normal" Angle up, right to the PE / PEN connection of the motor and to this an Angle up, left.
4. Position the motor so that the terminal strip with its bundle connection points and the motor connection points lie on the same line.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The following schematic is displayed:  
     
   ![](../Pictures/Visualisation/ALL/singlepole_kabelstrangerstellen5_av.png)
5. Select the menu items Insert > Bundle connection point > Angle.
6. Position the angle a small distance above the motor connection U1 and rotate it so that the thin connection points down and the thick connection (bundle connection point) points to the right.  
     
   ![](../Pictures/Gui/ALL/arrow.png) An autoconnect line leads from the bundle connection point to the motor connection point U1.
7. Click the left mouse button.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The Properties <...> dialog opens.
8. Select the Bundle connection point tab and enter "1" in the Bundle connection point designation field and, if desired, enter a Bundle connection point description.
9. If necessary, select the Display tab to define the display settings for the bundle connection point.
10. Click [OK].  
      
    ![](../Pictures/Gui/ALL/arrow.png) The Properties <...> dialog is closed. The angle is inserted into the schematic above the motor connection U1.
11. Repeat this process for another bundle connection point of type "Angle" and insert it at the same height above the extended PE / PEN terminal so that the thin connection points down and the thick connection points to the left.
12. Assign "4" as the Bundle connection point designation.  
      
    ![](../Pictures/Gui/ALL/arrow.png) The angle makes an autoconnect line with the PE / PEN connection point. In addition to this, the thick connection points of both inserted angles combine into a bundle.  
      
    ![](../Pictures/Visualisation/ALL/singlepole_kabelstrangerstellen6_av.png)
13. Now select the menu items Insert > Bundle connection point > T-node.
14. Rotate the T-node so that the thin connection points down and the thick connections point upwards.
15. Insert it above the motor connection point V1 and enter "2" as the Bundle connection point designation.
16. Insert another T-node below the motor connection W1 in the same manner and designate it with "3".  
      
    ![](../Pictures/Gui/ALL/arrow.png) The following schematic is displayed:  
      
    ![](../Pictures/Visualisation/ALL/singlepole_kabelstrangerstellen7_av.png)

### [ClosedConnect the bundle connection point groups and insert the cable definitions](javascript:void(0);)

In the third step, you connect both bundle connection point groups using suitable symbols.

1. Select the menu items Insert > Bundle connection point > Distributor, T-node.
2. Insert the symbol between the bundle connection points 2 and 3 of the terminal strip.
3. Insert another distributor T-node, rotated by 180°, between the bundle connection points 2 and 3 of the motors.  
     
   ![](../Pictures/Gui/ALL/arrow.png) A thick autoconnect line is shown between the distributor T-nodes - the bundle.
4. Finally, insert a cable definition line and drag it over all the autoconnect [lines](Glossary_o_leitungen.htm) between the bundle connection points and the terminal strip.
5. Enter "-W1" for the cable DT and assign any other desired [cable properties](Glossary_o_kabeleigenschaften.htm).  
     
   ![](../Pictures/Gui/ALL/arrow.png) The following schematic is displayed:  
     
   ![](../Pictures/Visualisation/ALL/singlepole_kabelstrangerstellen9_av.png)

See also

[Details on the Use of Cables in the Single-line Representation](singlepole_k_besonderheitenkabel.htm)

[Bundle Representation of Connections in Schematics](singlepole_k_straenge_in_einpoligerdarstellung.htm)

[Tab Bundle Connection Point](devicetaggui_r_stranganschluss.htm)