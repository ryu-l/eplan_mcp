# P501018: The dimensions 'Width' and 'Height' stored at the part do not agree with the dimensions of the macro <x> (<y> / <z>) (tolerance <u> percent)

### Cause

In the parts database to be checked a [part](Glossary_o_artikel.htm) was found at which a 2D window macro is stored whose dimensions deviate by a fixed specified maximum tolerance from the values of the parts [properties](Glossary_o_eigenschaften.htm) Height and Width entered at the part. EPLAN specifies the name of the macro in the placeholder <x>, the representation type in the placeholder <y>, the variant in the placeholder <z> and the used tolerance in the placeholder <u>.

### Solution

1. In the message management dialog mark the line with the message and select the Properties popup menu item.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The Parts management dialog is opened, the respective part is already marked in it.
2. Bring the Mounting data tab to the front.
3. Note the values in the fields Width and Height.
4. Change to the Technical data tab.
5. Remember the macro name entered in the Macro field.
6. Close the parts management.
7. Now place the macro of a schematic page of your check project and call the properties of the macro.
8. Remember the assigned values of the properties Width and Height in the Format tab.
9. Compare these values with the values already noted from the parts management.
10. Close the [property dialog](Glossary_o_eigenschaftendialog.htm).
11. Mark the line with the message in the message management dialog and open the parts management by means of the Properties popup menu item.
12. Change to the Mounting data tab for the part marked there and enter the dimensions from the macro into the Height and Width fields.
13. Close the parts management, save the modified data, and carry out a parts synchronization.
14. Then start a new check run.

![](../Pictures/Gui/ALL/note.png)Note:

Note that only the variant "A" is checked with regard to the dimensions in 2D [macros](Glossary_o_makros.htm).