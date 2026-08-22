# Inserting formulas into the parameters of installed components

Formulas must also be inserted for the parameters of the installed components:

1. Open the Axis Functionunit.
2. Select the installed Cylinder component.
3. Enter the following formula for the Symbol parameter:

```
=mc.$Symbol_Cylinder
```

1. Repeat steps 2 and 3 with the following data:

| Installed component | Parameter | Value |
| --- | --- | --- |
| Position\_1 | Symbol | =mc.$Symbol\_Position\_1 |
| Position\_2 | Symbol | =mc.$Symbol\_Position\_2 |
| Position\_3 | Symbol | =mc.$Symbol\_Position\_3 |
| Position\_4 | Symbol | =mc.$Symbol\_Position\_4 |

1. Repeat steps 1 and 3 for the following Function units:

| Functionunit | Installed component | Parameter | Value |
| --- | --- | --- | --- |
| Gripper | Valve | Symbol | =mc.$Symbol\_Valve |
| Pressuresensor | Symbol | =mc.$Symbol\_Pressuresensor |
| Orientationinspector | Positionssensor\_optical | Symbol | =mc.$Symbol\_Position\_1 |
| Separator | Cylinder | Symbol | =mc.$Symbol\_Cylinder |
| Position\_1 | Symbol | =mc.$Symbol\_Position\_1 |
| Position\_2 | Symbol | =mc.$Symbol\_Position\_2 |
| Stack | Positionssensor\_optical | Symbol | =mc.$Symbol\_Position\_1 |