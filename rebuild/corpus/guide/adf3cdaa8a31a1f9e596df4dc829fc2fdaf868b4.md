# Numbering of Nested Devices

When numbering superior devices containing subordinate devices, usually only the superior device is numbered.

![](../Pictures/Gui/ALL/example.png) [![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

- Identifier: K, U, X, A
- Start 10, increment 10

| Displayed DT | Function text | Preview of result | Final results |
| --- | --- | --- | --- |
| =A+O-K1 | Contactor coil | K10 | =A+O-K10 |
| =A+O-U1 | Black box 1 | U10 | =A+O-U10 |
| =A+O-U1-K9 | Contactor coil nested inside black box 1 | This element is suppressed in the result preview. | =A+O-U10-K9 |
| =A+O-U1-X2 | Nested terminal strip | U10 | =A+O-U10-X2 |
| =A+O-U1-A9-X2 | Nested PLC with nested terminal strip | U10 | =A+O-U10-A9-X2 |
| =A+O-U1-A9-X2 | Nested PLC with terminal strip nested inside black box 1 | This element is suppressed in the result preview. | =A+O-U10-A9-X2 |
| =A+O-U2-K9 | Contactor coil nested in DT | U20 | =A+O-U20-K9 |