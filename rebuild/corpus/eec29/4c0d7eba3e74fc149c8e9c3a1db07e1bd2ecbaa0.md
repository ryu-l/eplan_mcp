# IF

IF checks the truth value of a condition, which is described by a formula. If the truth value is true then the condition is satisfied and the following operation is executed. If the truth value is false then the following operation is skipped. Further conditions can be expressed with ELSE, whose truth value is checked afterwards.

ELSE checks the truth value of a further condition after the result of a previous condition is false. ELSE is optional, that means, for example, if in the ELSE case no text is created, then the ELSE branch may be omitted.

END\_IF ends the control structure.

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

```
(*{IF $Group="Cyclic"}*) true
(*{ELSE}*) false
(*{END_IF}*)
oder:
(*{IF $Group="Cyclic"}*) true
(*{END_IF}*)
```