# Name of the unit for global parameters

Path to model variable:

Model Variables > Disciplines

Specify a string value. The value determines the unit in which a search for parameters is first carried out while discipline resources are Import and synchronized before these are created in the unit for the respective discipline parameters.

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

Requirements:

Definition of model variables:

| Name | Value |
| --- | --- |
| Disciplines > Global [Parameter](glossary_o_parameter.htm) [Unit](glossary_o_unit.htm) | Parameter pool |
| Disciplines > ECAD Parameter Unit | ECAD.Parameter |
| Disciplines > ECAD > Create parameters on demand | true |

The Parameter pool unit contains at least one parameter with the Position name.

The ECAD.Parameter unit contains a parameter with the Location name.

An ECAD discipline component is created. This contains the parameters Position, Location and Page.

Result:

- The Position parameter references the parameter by the same name in the Parameter pool unit.
- The Location parameter references the parameter by the same name in the ECAD.Parameter unit.
- The Page parameter is created in the ECAD.Parameter unit.