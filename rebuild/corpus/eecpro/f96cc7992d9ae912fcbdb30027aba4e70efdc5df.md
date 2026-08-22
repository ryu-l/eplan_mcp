# Generating the current status of the schematic

This test shows that by determining the values for the plugs and sockets by way of the formulas, all sensors can initially be placed again. If the Inspect function group is deactivated, there must not be any gaps between the sensors.

1. Generate the ECAD structure again.

![](../Pictures/tutp8_generateSchematicResult_4.png)

2. The structure consists of 2 pages that contain 8 or 2 sensors.
3. Open the schematic again.

![](../Pictures/tutp8_generateSchematicResultP8_3.png)

4. The schematic consists of 2 pages where all sensors are available.
5. The pages now have names.
6. Close P8 and disable again the Inspect function group by setting the Option\_Inspect\_available to false.
7. Generate the ECAD structure once again.

![](../Pictures/tutorial_p8_test5_ergebnis_struktur.png)

8. The schematic consists of the PLC\_Sensors\_1\_8\_Feeder page that contains 7 sensors, and the PLC\_Sensors\_9\_16\_Feeder page that does not contain any sensors.
9. Open the schematic again.

![](../Pictures/tutp8_generateSchematicResultP8_4.png)

10. On the first page of the schematic, one can see that the PLC inputs are now assigned without any gaps. On the second page, all PLC inputs are unconnected. Thus, the second page is not required, and is to be disabled by means of a formula in the next step.

Upon closer inspection, one can see that the device tags and function texts are still represented by <null>. For these elements, too, formulas must still be entered.

![](../Pictures/tutorial_p8_sensoren_bmk_null.png)