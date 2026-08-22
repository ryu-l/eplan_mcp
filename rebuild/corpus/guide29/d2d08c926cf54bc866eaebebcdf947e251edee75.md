# Globally Editing the Properties for all Representations of an Auxiliary Function

An auxiliary function can be represented more than once in the project, as a distributed single-line, multi-line, overview, pair cross-reference function, and / or a [P&I diagram](Glossary_o_ri_fliessbild.htm) function. The "Properties (global)" feature allows you to change the common [properties](Glossary_o_eigenschaften.htm) for all function representations of one auxiliary function at the same time, e.g., the function text of all function representations of an NO contact.

Preconditions:

- You have opened a project.
- You have opened the graphical editor or the device navigator.

1. To globally edit the properties of an auxiliary function in the device navigator, select the function representation of an auxiliary function and then select Popup menu > Properties (global).  
    To globally edit the properties of an auxiliary function in the graphical editor, in the Options menu, select the Properties (global) menu item and then double-click the function representation of an auxiliary function.  
      
    ![](../Pictures/Gui/ALL/arrow.png) In the Properties (global): <...> dialog, the <Function category> tab is labeled with the function category of the corresponding function definition, e.g., <NO contact> or <Safety fuse>.
2. Change the desired properties of the auxiliary function.
3. Click [OK].
4. Press [F5] to update.   
      
    ![](../Pictures/Gui/ALL/arrow.png) The properties are changed at all associated function representations of the selected auxiliary function.

![](../Pictures/Gui/ALL/note.png)Note:

In the Properties (global) editing mode, you cannot edit the Displayed DT because the displayed DTs of the individual function representations can differ. In this case, the field is not available. However, if you change the Full DT then the displayed DT is automatically derived from this. In the <Function category> tab you can change the Full DT for all function representations of the auxiliary function. These function representations then no longer belong to the device. Or, in the <Function category> (device) tab, you can change the Full DT for the entire device.

See also

[Globally Editing the Properties for all Representations of a Main Function](reverseengineering_h_alledarstellungenbm.htm)

[Editing the Properties of the Selected Function Representation](reverseengineering_h_ausgewaehltefunktion.htm)

[Globally Changing the DT at Functions](devicetaggui_h_bmkaendern.htm)