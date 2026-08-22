# Assign formula to Disabler for the second page

A formula for the Disabler must be entered to prevent an empty page in the schematic when the Testing function group is disabled.

1. In T\_Mechatronic\_ModularSystem, open the Feeder component.

![](../Pictures/tutorial_p8_disabler_seite2.png)

1. Highlight the PLC\_Sensors\_9\_16 component.
2. Enter the following formula in the Disabled field:

```
=not(mroot.rmos('T_Mechatronic_ModularSystem.ECAD.PLC_Inputs.abstract_Sensor').size > 8)
```

This formula determines whether the total number of (abstract) sensors is greater than 8 (.size > 8). If the number is less than 8, the page is disabled; otherwise, it is active.