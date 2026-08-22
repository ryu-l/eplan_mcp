# Combining Elements Into a Block / Breaking up a Block

You can use the two commands Form block and Break up block to combine graphical elements of a page (e.g. [lines](Glossary_o_leitungen.htm), circles, etc.) into a block, or break up an existing block into its original individual elements.

Combining individual records into a single record in this way reduces the storage requirements and increases the database access speed. When forming a block, the following cases are handled differently:

- The collection of selected elements contains only graphical [objects](Glossary_o_objekte.htm) and language-neutral texts:  
   In this case, a block is created containing the selected graphical objects. A block reference that graphically represents this block is also inserted into the page.
- The collection of selected elements contains one [component](Glossary_o_schaltzeichen.htm) and several graphical objects or language-neutral texts:  
   Here too, a block is formed from the graphical objects, but the graphic just appears as [part](Glossary_o_artikel.htm) of the component. Other than this, the component behavior is unchanged.

Precondition:

You have opened a page, [form](Glossary_o_verlauf.htm), plot frame or symbol.

1. Select the graphical elements that are to be combined into a block and then select the menu item Edit > Other > Form block.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The selected elements are combined to a block and the objects can no longer be individually edited.  
     
   ![](../Pictures/Gui/ALL/arrow.png) If objects in the collection of selected elements are grouped, then the grouping is automatically removed before the block is generated.   
     
   ![](../Pictures/Gui/ALL/arrow.png) If the collection of selected elements contains more than one logical object and/or language-neutral texts then a message is displayed and the block formation is canceled.
2. Select the block that you wish to break up and then select the menu item Edit > Other > Break up block.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The block is broken up into its elements and the objects can now be individually edited once more.

See also

[Dialog Edit block reference properties](gededitgui_d_blockreferenzeigenschaften.htm)

[Graphical editor](gededitgui_k_start.htm)