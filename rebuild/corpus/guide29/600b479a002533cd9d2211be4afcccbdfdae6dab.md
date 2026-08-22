# Device Logic: Principle

3D [objects](Glossary_o_objekte.htm) that are to be used as mechanical or electromechanical [devices](Glossary_o_betriebsmittel.htm) in the 3D mounting layout must have a range of [properties](Glossary_o_eigenschaften.htm) that allow them to be used in the mounting layout:

- The objects can be placed in the [layout space](Glossary_o_bauraum.htm) and on other objects.
- Other objects can be placed on the 3D objects.
- The placed objects fit in with the logical structure of the [items](Glossary_o_bauteile.htm).

All these properties in their entirety are known as the device logic. There are a number of [functions](Glossary_o_funktionen.htm) available for creating and editing the device logic. These functions are used following the use of graphical import and editing functions and prepare the 3D graphic - which immediately after import has no logic functions - for use as a 3D [macros](Glossary_o_makros.htm) for devices. To ensure correct placement it is necessary as a minimum to define a placement area; the other logic functions are optional.

### Graphic definition for devices

The following functions define a 3D graphic:

- Layout space > Import (3D graphic)
- Edit > Graphic > Unite
- Edit > Graphic > Rotate around axis

These functions can be used in the schematic project and in the 3D macro project.

### Logic definition for devices

The following functions define the device logic. They can be accessed under the Edit > Device logic menu items.

- Placement area > Define / Turn around / Move / Rotate: Definition of an area on an item on which the 3D object itself is placed and aligned. Placement areas can only be defined, displayed and edited in a macro project.

The following functionalities can be used in the schematic project and in the macro project and be displayed by using View > Mounting aids:

- Mounting point: Definition of points which as 3D snap points allow other components to [dock](Glossary_o_andocken.htm) to the 3D object.
- Mounting line: Definition of [lines](Glossary_o_leitungen.htm) on non length-variable items on which components can be placed. These lines can have an alignment in which the items can be rotated on placement.
- Mounting surface: Definition of surfaces on which components can be placed; these surfaces are found by automatic activation or can be selectively activated.
- Mounting grid: Definition of a [grid](Glossary_o_raster.htm) which allow other components to dock to the 3D object.
- Handle: Definition of points by which the 3D object is moved on the cursor on placement; these points can dock to 3D snap points of other 3D objects when placed.
- Base points: Definition of points on which accessory parts can be placed automatically at fixed defined positions in enclosures.

Mounting points, mounting lines, mounting grids and base points can be moved in [macro projects](Glossary_o_makroprojekte.htm) like graphical elements by using Edit > Move or via "Drag & Drop".

### Handles and mounting points: Interactive points, lines, and areas in the device logic

The functions for defining the device logic work with interactive points, lines, and areas. User-defined points and surfaces can be used to [create](Glossary_o_erstellen.htm) dependencies in the assembly of 3D components. Interactive points can also be added if necessary to components that have been imported from external 3D CAD systems using the STEP exchange format, to control [placing](Glossary_o_auflegen.htm) options or to define degrees of freedom in the rotation and alignment of components to one another.

Interactive points always consist of two corresponding parts:

- Handles look for associated [mounting points](Glossary_o_montagepunkte.htm). They define points or areas which can only be moved and placed on the corresponding mounting points.
- Mounting points, mounting lines, mounting grids and mounting surfaces only allow the associated handle to be snapped to, moved to and placed on them. Mounting points may be points, lines, or areas.

Color coding:

| Points | Display |
| --- | --- |
| Handle ([user-defined](Glossary_o_benutzerdefiniert.htm)) | Orange cuboid |
| Handle (default) | Red cuboid |
| Mounting point (user-defined) | Green cuboid |
| Mounting point (default) | Blue cuboid |
| Base point | Cyan cuboid |

Defined interactive points can be displayed and edited via the View > Mounting aids menu items. Mounting points can be freely configured in the [property dialog](Glossary_o_eigenschaftendialog.htm).

See also

[Defining a Mounting Surface](cabinetgui_h_montageflaechedefinieren.htm)

[Defining a Handle](cabinetgui_h_anfasspunktdefinieren.htm)

[Defining Mounting Points](cabinetgui_h_zielmatesdefinieren.htm)

[Defining Mounting Lines](cabinetgui_h_montageliniedefinieren.htm)

[Defining and Using a Mounting Grid](cabinetgui_h_montagerasterdefinieren.htm)

[Defining and Changing Placement Areas](cabinetgui_h_einbauflaeche.htm)

[Defining a Base Point](cabinetgui_h_bezugspunktdefinieren.htm)