# Exporting, backing up and importing data for a Client-Server installation

The steps to export, back up and import data are not markedly different form those of the Stand-Alone installation.

The only differences are:

- With a client-server installation, you must export the preferences for each user.
- You must back up the file ec.ini, and copy it back to the installation folder after the new installation.

In particular, proceed as follows:

1. Export and back-up the data from the existing installation as you would for a stand-alone installation (see Exporting the current information model).
2. Back-up the file ec.ini  (located in the EEC installation folder).
3. Remove the existing installation.
4. Install the new EEC version.
5. Copy the backed-up ec.ini back to the EEC installation folder.
6. Use the program ec\_admin.exe to delete the demonstration database (see [Removing a database](admin_h_maintenance_database_remove.htm)).
7. Use the program ec\_admin.exe to create a new database (see [Creating a database](admin_h_maintenance_database_creation.htm)).
8. Import the backed-up data by using the program ec\_admin.exe (see [Importing model data](admin_h_maintenance_model_import.htm)).
9. Use the program ec\_admin.exe to update the model (see [Updating a model](admin_h_maintenance_model_update.htm)).
10. Apply the resources from the compressed resource folder (see [Restoring resources](admin_h_backup_recover_resources.htm)).
11. Apply the preferences (see [Restoring preferences](admin_h_backup_recover_user_settings.htm)).

![](../Pictures/Gui/ALL/note.png)Note:

The user preferences have to be applied for each user separately.