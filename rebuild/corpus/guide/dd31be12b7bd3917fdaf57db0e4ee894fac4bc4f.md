# Synchronize master data

The master data (for example a symbol library) are not referenced but stored in the project, this means copied into it. The storage of the master data used thus takes place in the Project. Depending on the project settings specified under File > Settings > Projects > "Project name" > Management > General, File > Settings > Projects > "Project name" > Management > Symbol libraries and File > Settings > Projects > "Project name" > Reports > Display / output you can, if required, manually start the synchronization of project master data with the system-specific data.

![](../Pictures/Gui/ALL/note.png)Note:

The master data comparison is not case-sensitive with regard to file names. The file name ABC.XYZ is identical to abc.xyz.

Preconditions:

- You have opened the project whose master data is to be synchronized.
- You have no editor open for working on master data (Plot frame editor, Form editor, etc.).

### Synchronize individual master data objects

1. Select the following commands: Tab Master data > Command group Synchronization > Synchronize project.
2. In the Synchronize master data - <project name> dialog click the column headers in the tables in order to sort the data alphanumerically in either ascending or descending order by column. For example, if you click the column Type, all entries will be sorted and displayed according to the Master data type.
3. In the Project master data list select the master data objects that you would like to transfer to the system master data. Multiple selection is possible.
4. Click ![](../Pictures/Gui/ALL/all_arrowright_as.png).
5. In the System master data list select the master data objects that you would like to transfer to the project master data. Multiple selection is possible.
6. Click ![](../Pictures/Gui/ALL/all_arrowleft_as.png).
7. Click [Close].

![](../Pictures/Gui/ALL/note.png)Note:

In both actions, Eplan informs you in a message window as to how many project / system master data files were updated and, if the project / system master data were identical, in which a message is also generated.

### Globally synchronize master data

1. Select the following commands: Tab Master data > Command group Synchronization > Synchronize project.
2. In the Synchronize master data - <project name> dialog select [Update] > Project in order to globally replace all outdated project master data with newer system master data.
3. Select [Update] > System to globally replace all outdated system master data with newer project master data.
4. Click [Close].

![](../Pictures/Gui/ALL/note.png)Notes:

- In both actions, Eplan informs you in a message window as to how many project / system master data files were updated and, if the project / system master data were identical, in which a message is also generated.
- When updating Symbol libraries the files in question are checked for compatibility (e.g., regarding connection point designations). If they are not compatible, the process will be interrupted with a prompt.