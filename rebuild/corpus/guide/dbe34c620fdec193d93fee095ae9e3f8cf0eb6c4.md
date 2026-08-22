# P026017: The structure identifier does not correspond to the mounting surface

### Cause

You created specific project structure and defined identifierblocks to which you assigned structure identifiers. Now there are conflicting structure identifiers for the placed part and for the corresponding mounting surface, in one of the identifier blocks.

### Solution

1. Enter the same structure identifiers for the relevant identifier blocks (for example for "Function designation" and / or "Location designation") for the part placement and the corresponding mounting surface (in the Properties <...> dialog in the Displayed DT field).
2. If required, start a new check run.