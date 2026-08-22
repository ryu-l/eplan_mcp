# Creating Planning Objects, PCT Loops, PCT Loop Functions, Containers and Connection Planning Objects

Planning [objects](Glossary_o_objekte.htm) are created and managed in the pre-planning navigator. [PCT loops](Glossary_o_plt_stellen.htm), [PCT loop functions](Glossary_o_plt_stellenfunktionen.htm), containers, connection [planning objects](Glossary_o_planungsobjekte.htm) (piping planning objects, [cable](Glossary_o_kabel.htm) planning objects) are created in the same way as general planning objects and are managed parallel to these. You specify the type of planning object that you [create](Glossary_o_erstellen.htm) through the segment definition.

![](../Pictures/Gui/ALL/note.png)Note:

PCT loop [functions](Glossary_o_funktionen.htm) can only be created below PCT [loops](Glossary_o_messstellen.htm).

When PCT loops and PCT loop functions are created, the [settings](Glossary_o_einstellungen.htm) for PCT loops specified in the project settings are followed in the pre-planning (under Options > Settings > Projects > "Project name" > Pre-planning > PCT loops). Use this dialog, for example, to specify the [properties](Glossary_o_eigenschaften.htm) that are to be identifying besides the "Number" and the plant [levels](Glossary_o_etagen.htm) that allow for identical PCT loops.

1. Select the following menu [items](Glossary_o_bauteile.htm): Project data > Pre-planning > Navigator
2. Highlight the project, a structure segment or an existing planning object, and select the popup menu item New planning object.
3. Select the desired segment definition in the dialog Select segment definition.  
     
   ![](../Pictures/Gui/ALL/arrow.png) Depending on the selected hierarchy level, [segment definitions](Glossary_o_segmentdefinitionen.htm) for planning objects, PCT loops, containers, piping planning objects or cable planning objects are displayed for selection. If you have selected a PCT loop, only segment definitions for PCT loop functions are displayed.
4. Click [OK].
5. Enter the desired data for the new planning object in the Properties <...> dialog. To do so, bring the first tab to the front in the [property dialog](Glossary_o_eigenschaftendialog.htm).  
     
   ![](../Pictures/Gui/ALL/arrow.png) At PCT loops and PCT loop functions the PCT loop number is combined automatically from the entries in the Designation group box.
6. Enter the [designations](Glossary_o_bezeichnungen.htm) of the [segments](Glossary_o_segmente.htm) that are to represent the source and target of the connection planning object for a connection planning object. To this purpose the fields Source segment and Target segment are available for piping planning objects, and the properties of the same name are available for cable planning objects. In both cases you can also select source and target segments by using the [â¦] button.
7. Click [OK].  
     
   ![](../Pictures/Gui/ALL/arrow.png) A planning object is created with the corresponding properties.

![](../Pictures/Gui/ALL/info.png)Tip:

When creating connection planning objects you can initially leave the Source segment and Target segment fields empty. The source and target of a connection planning object are then determined automatically later on during placement on a pre-planning page.

See also

[Pre-planning: Principle](planninggui_k_prinzip.htm)

[Connection planning objects](planninggui_k_verbindungsvorplanung.htm)

[Dialog Settings: PCT loops (pre-planning)](planninggui_d_einstellpltstellen.htm)

[Creating planning objects as devices](planninggui_h_planungsobjektmitartikel.htm)

[Creating Graphical Pre-planning](planninggui_h_grafvorplanungerstellen.htm)