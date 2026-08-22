# Model variables for the parts database

In order to work with EPLAN Pro Panel, it must be possible to access the parts database. There are corresponding methods for this in the formula language, as well as model variables. The advantage of model variables is that SQL databases can be addressed as well, and the required data can be determined before generation begins.

![](../Pictures/Gui/ALL/note.png)Note:

These model variables are not assigned to parameter names, but the required values are directly entered.

The model variables are located at Disciplines > ECAD > EPLAN Electric P8 > Parts database:

| Model variable | Example value |
| --- | --- |
| Access Database File | Parts\CompanyName\ESS\_part001.mdb |
| SQL Catalog |  |
| SQL Password |  |
| SQL Server |  |
| SQL Username |  |

Access to the database can be carried out either by a database user who has to carry out corresponding specifications for authorizations, or by a user who authorizes themselves through their Windows login. The following tables show which specifications are required respectively (values are only examples).

The following specifications are required in the case of a Windows authorization:

| Model variable | Value |
| --- | --- |
| Access Database File |  |
| SQL Catalog | DataBaseName |
| SQL Password |  |
| SQL Server | ServerName\SQLEXPRESS |
| SQL Username |  |

The following specifications are required in the case of an SQL Server Authentication:

| Model variable | Value |
| --- | --- |
| Access Database File |  |
| SQL Catalog | DataBaseName |
| SQL Password | \*\*\* |
| SQL Server | ServerName\SQLEXPRESS |
| SQL Username | LoginName |

The password is displayed represented by asterisks.