# de.eplan.eec.jobserver.worker.jobdefinitionsfolder

The following EEC argument must be transferred with the following syntax:

```
-D<Argument>=<Value>
```

| EEC argument | Usage |
| --- | --- |
| -Dde.eplan.eec.jobserver.worker.jobdefinitionsfolder=<Path name (UNC)> | Only for Worker |
| **Annotation** | |
| The file folder where job definitions for this Worker are stored. The folder can also be specified as a [UNC path](glossary_o_unc.htm).  Example:   ``` -Dde.eplan.eec.jobserver.worker.jobdefinitionsfolder=\\myShare\jobserver\jobdefinitions ``` | |