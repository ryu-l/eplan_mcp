# P005021: Potential definition with incorrect potential

### Cause

A potential definition point was placed on a connection and equipped with a potential and a signal name. The potential is, however, not placed at any location of the schematic via a potential definition or via a potential connection point. Or only a signal name but not a name of potential was entered at a potential definition point.

### Solution

#### Possibility 1

1. Locate the potential definition point in the schematic by using the Go to (graphic) functionality from the popup menu in the Message management dialog.
2. Call up the property dialog of the potential definition point.
3. Assign the potential name of an existing potential definition point or potential connection point that has only one potential name to the faulty potential definition point.

#### Possibility 2

1. Define a new potential in the schematic, using, for example, a potential connection point.
2. Assign the name of the potential definition point for which you defined the signal name to this connection point.

---

  

If required, start a new check run.