# de.eplan.eec.datasource.user

The EEC argument must be transferred with the following syntax:

```
-D<Argument>=<Value>
```

| EEC argument | Usage |
| --- | --- |
| -Dde.eplan.eec.datasource.<absolute path to datasource object>.user=<user name> | Optional |
| **Annotation** | |
| By means of EEC arguments for the runtime environment the entries Connection URL, User, Password and Default table for a database component of the DatabaseDataSource type could be overruled.  By means of the EEC argument de.eplan.eec.datasource.<absolute path to datasource object>.user the user name of the database is given.  Example:  A different user of the database of the datasource component Databases.SQL.PartsDB should the assigned.   ``` -Dde.eplan.eec.datasource.Databases.SQL.PartsDB.user=John ``` | |