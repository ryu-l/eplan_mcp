# P005084: The substance '<x>' property of the connection contradicts the piping definition

### Cause

The P&I diagram contains a connection on which a piping definition (piping connection point or piping definition point) is placed. The connection and the piping definition have different values for the Substance property. For example the substance "Water" was entered at the connection definition point of the connection, while the substance "Air" was entered at the piping definition.

### Solution

1. Locate the connection definition point of the connection in the P&I diagram using the Go to (graphic) functionality from the popup menu in the Message management dialog.
2. Jump to the piping definition by means of the Go to (2nd Coordinate) option of the popup menu.
3. Determine the value entered in the Substance field in the respective property dialog.
4. Standardize the two values or delete the value at the connection definition point.
5. If required, start a new check run.