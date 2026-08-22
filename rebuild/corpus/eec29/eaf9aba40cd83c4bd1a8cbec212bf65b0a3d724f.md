# Removing a database from a server

A server-based database is used in connection with a client-server installation. It is deleted using the administration tool.

![](../Pictures/ec_admin_erstelle_server_datenbank.png)

1. When removing a database from a server, the check box Client-Server Installation must be enabled.
2. The host must be the available server in the corresponding notation.

Upon entry of the host name and / or port number, their availability will be checked immediately (4). If the port number is entered slowly, the availability check will be carried out character by character, which may cause a delay. Using [F5], the availability check can be executed on the entire entry, thus accelerating the process.

3. The name of the database to be removed must be entered in the Databasename field.
4. The database is removed via [Remove Database].