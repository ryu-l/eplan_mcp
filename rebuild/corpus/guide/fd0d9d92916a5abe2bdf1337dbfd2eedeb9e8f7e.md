# Updating Main Elements

Synchronization problems can occur if the part placements are created first, and then the components as there may be different data stored for the placements. If this occurs, the main function generally has no part references, even though there may be one or more suitable part placements for the device. This menu option allows all the part references for all the associated part placements to be transferred to the main function; the device to be updated must be selected in the graphical editor or the panel layout navigator.

Precondition:

You have opened a project.

1. Select the following commands: Tab Devices > Command group 2D panel layout > Navigator.
2. In the 2D panel layout - <Project name> dialog, select the part placements to be updated.
3. Select the Update main elements popup menu item.  
     
   ![](../Pictures/Gui/ALL/arrow.png) Eplan displays a warning indicating that this action will result in deleting all parts data at the main functions of the selected devices and in replacing this data by the data of the associated part placements.
4. If you really want to execute this action, click [Yes].  
     
   ![](../Pictures/Gui/ALL/arrow.png) The elements are updated.