# Create parameter

You create parameters within a library. To organize the parameters, you can create any structures using units. You create a new parameter via the popup menu of a unit or another object.

Parameters are typed, i.e., there are different types of parameters that differ from each other in terms of the values assigned to them. For example, there are parameters for integers, strings or truth values (Boolean). To distinguish between two variants, one truth value will be enough, that is, a parameter of the Boolean type, which can assume the two values true or false.

To create a new parameter:

![Create parameter step 1](../Pictures/createParameter_1.png)

1. Call up the popup menu of a library or a unit and select New > Engineering > Parameter.

![Create parameter step 2](../Pictures/createParameter_2.png)

1. Enter a name for the new parameter.

### Note

The name of a new object should not contain a special character (){}[].:,;-/\Â§$%&#~<>|= so that on the one hand it is file system-compliant and on the other hand no problems occur during the creation of formulas.

1. Enter a type or select a type via [..].
2. Enter a comment optionally.
3. Save with [Ctrl] + [S] or ![](../Pictures/speichern.png).

The component is created as a result of the assignment of a name and subsequently the saving of the editor. Without a valid name the name field is highlighted in red. A name must be unique within a unit.

If a given value does not conform to the type of the parameter, the result field is highlighted in red and a corresponding message is entered in the message log.