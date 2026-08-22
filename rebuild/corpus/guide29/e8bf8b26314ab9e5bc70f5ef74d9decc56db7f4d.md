# Automatically Assigning Page Information

The Format for automatic page description [form](Glossary_o_verlauf.htm) property can be used to specify the page information (page name, page description, [higher-level function](Glossary_o_anlage.htm), etc.) for the page description automatically assigned when generating [reports](Glossary_o_auswertungen.htm).

Preconditions:

- You have opened a project.
- You have opened the form whose [properties](Glossary_o_eigenschaften.htm) you would like to edit in the form editor (Utilities > Master data > Form > Open > [Open]).
- You have opened the Form properties - <Form name> dialog (Popup menu > Properties in the form in the navigator dialog Pages - <Project name>).

1. Click [...] in the Value column of the Format for automatic page description property of the Form properties - <Form name> dialog.
2. In the Format for automatic page description dialog, select the element that should be used for the automatic page description from the Available format elements list. (Multiple selection isn't possible here).
3. Click ![](../Pictures/Gui/ALL/all_arrowright_as.png) (Move to the right).  
     
   ![](../Pictures/Gui/ALL/arrow.png) The element is adopted in the Selected format elements list.
4. Proceed in a similar way for all additional [format elements](Glossary_o_formatelemente.htm).
5. Click ![](../Pictures/Gui/ALL/all_arrowup_as.png) (Move up) / ![](../Pictures/Gui/ALL/all_arrowdown_as.png) (Move down) to move a selected format element up or down, if possible. (Selection of multiple elements is not possible here, and the format element of type Separator between header objects cannot be moved because it is always automatically inserted at the end of the list.)
6. Click [OK].  
     
   ![](../Pictures/Gui/ALL/arrow.png) The format elements are saved.

The format elements are displayed as follows in the Value column of the Form properties - <Form name> dialog:

<Number of the available format element>;<Number / Length / Property ID>|<Number of the available format element>;<Number / Length / Property ID>|... 
  
with the numbers being assigned as follows:

- Page type / form type: 1
- Form properties: 9
- Name of header object: 2
- Other properties of header object: 10
- Name of first data object: 3
- Name of last data object: 4
- Separator: 5
- Separator between header objects: 11

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

2;1|9;<18000,0>|5;4 for:  
Name of header object, Number / Length: 1  
Form properties, Property Name (form, plot frame, outline, form (copper)) ([ID](Glossary_o_id.htm) 18000, Index 0)  
Separator, number / length: 4