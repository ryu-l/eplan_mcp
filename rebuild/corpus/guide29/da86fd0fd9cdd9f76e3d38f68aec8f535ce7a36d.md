# Placing Symbols

You can place a given symbol once or several times on schematic pages in the graphical editor, however you cannot select multiple different [symbols](Glossary_o_symbole.htm) for a single placement operation.

A preview of the autoconnection [lines](Glossary_o_leitungen.htm) is shown in the graphical editor, which shows where a connection from one symbol to another symbol is possible. As an extra aid for placement, a line is also shown between the first placed symbol and the current cursor position. This allows you to place symbols along a line.

Insertion points and [connection points](Glossary_o_anschluesse.htm) pointing in the same direction may not lie on top of each other. If this occurs when inserting a symbol then an error message is displayed and the action is canceled. (Exceptions to this are symbols containing opposing connection points laid on top of each other at the same point, e.g. T-connectors.)

Precondition:

You have opened a project. You have opened a project page in the graphical editor.

1. Select the following menu [items](Glossary_o_bauteile.htm): Insert > Symbol
2. Select the desired symbol in the Symbol selection dialog.
3. For faster selection, click [...] in the Filter field if necessary, and then select the filter criteria or [create](Glossary_o_erstellen.htm) new ones.
4. Or enter a character string in the Direct entry field in the list view.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The cursor jumps to the first symbol matching your entry as soon as you enter a single character, and selects it.
5. Select the popup menu item Function-oriented in the tree view if the hierarchical display of the symbols should not be carried out according to the symbol library, but according to their functional Category (such as "Coils and contacts", "Signal [devices](Glossary_o_betriebsmittel.htm)", etc.).
6. In the list view select the popup menu item Configure representation if you would like to change the display and / or the sequence of the symbol [properties](Glossary_o_eigenschaften.htm) in the list.
7. Click [OK].
8. Place the symbol in the schematic.  
     
   ![](../Pictures/Gui/ALL/arrow.png) If you position the symbol above or below a connection element or another symbol, a preview of the autoconnection lines is displayed. After being placed the symbol is connected automatically with the other element in the schematic.
9. Specify the device-specific properties in the Properties <...> dialog.
10. Click [OK].

![](../Pictures/Gui/ALL/info.png)Tip:

If you want to determine the assignment of connection points, place the symbol and number the [connection point designations](Glossary_o_anschlussbezeichnungen.htm) consecutively. To do so, manually enter the connection point [designations](Glossary_o_bezeichnungen.htm) - separated by a paragraph mark each - in the first tab of the properties dialog in the Connection point designation field. Display in the graphical editor will then show the sequence of the function [connections](Glossary_o_verbindungen.htm) according to the connection point logic.

### Multiply connecting symbols with other symbols in the schematic

1. Select the following menu items: Insert > Symbol
2. Select the desired symbol in the Symbol selection dialog.
3. Click [OK].
4. Use the cursor to position the symbol above or below a connection element. Click the left mouse button and keep it pressed.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The autoconnect lines preview is displayed.
5. Move the cursor to the left or right in the schematic page while keeping the left mouse button pressed.  
     
   ![](../Pictures/Gui/ALL/arrow.png) A preview of the autoconnection lines is displayed for all positions where a connection to a symbol lying above or below the line is possible.
6. Release the left mouse button.  
     
   ![](../Pictures/Gui/ALL/arrow.png) The symbols are placed and connected with the other symbols in the schematic. In this case, the Properties <...> dialog is not opened and the [component](Glossary_o_schaltzeichen.htm) properties are taken from the default [settings](Glossary_o_einstellungen.htm) and the current numbering mode.

See also

[Dialog Symbol selection](xsbgui_d_symbolauswahl.htm)

[Preventing a New Placement of a Symbol](xsbgui_h_symbolplatzierungverhindern.htm)

[Connection Point Designations and Descriptions](gededitgui_h_anschlussbezanzeigen.htm)