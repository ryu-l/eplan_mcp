# Script syntax

Scripts are created in native Java.

The following rules apply to strings that contain a $ character. If the string is emphasized by double quotes, the properties of the object are accessed in Groovy, similar to the accessing of parameters in EEC. This produces a string that contains the result of this access. In order to display the $ character in a string, the string must be emphasized by single quotes.

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example code:](javascript:void(0);)

```
String w = 'world';
String s1 = 'Hello $w';
String s2 = "Hello $w";
System.out.println(s1); // -> Hello $w
System.out.println(s2); // -> Hello world
```

The s1 variable saves the string in a character-perfect manner. In the case of the s2 variable, the w variable is resolved, and the value is inserted.

Existing scripts in which formulas with parameter access are defined in this manner must be checked for notation and modified if necessary to avoid any problems.