# Parameter ImportParameter

The ImportParameter parameter contains individual parameters to be passed.

Syntax:

```
=Map{
	Pair{'HEADDATA',List{List{'MATERIAL','IND_SECTOR','MATL_TYPE','BASIC_VIEW'},
	List{mc.$MaterialNumber,mc.$MaterialSector,mc.$MaterialType,'X'}}},
	Pair{'CLIENTDATA',List{List{'BASE_UOM','BASE_UOM_ISO'},List{'ST','ST'}}},
	Pair{'CLIENTDATAX',List{List{'BASE_UOM','BASE_UOM_ISO'},List{'X','X'}}}
}
```