# Importing model data

If a new database is created, it has at first no content and is thus not suitable yet to be used with EEC.

Therefore, the creation of a database is supported by a wizard that imports model data after the database has been created.

![](../Pictures/ec_admin_importiere_modelldaten.png)

1. In the Import field, a file must be entered that corresponds to the Mind XML format.

The file system can be searched for a suitable file via [Browse...]. If a file is selected that does not correspond to the Mind XML format, an error message will be displayed.

![](../Pictures/ec_admin_falsches_format.png)

2. In the TXN Limit field, the number of data sets is entered that can be written to the database per transaction. The default is 10000. Smaller values mean fewer temporary data in the RAM, but slow down the import. Greater values accelerate the import, but create larger temporary data volumes in the RAM.
3. [Finish] starts the import of model data.