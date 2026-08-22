# P005037: Conflicting intrinsic safety of connection points

### Cause

The target [functions](Glossary_o_funktionen.htm) for a connection contradict one another with respect to the Intrinsically safe property. For example, in the function [settings](Glossary_o_einstellungen.htm) of one target the Intrinsically safe check box was selected and the setting Intrinsic safety possible was defined for the function [connections](Glossary_o_verbindungen.htm). On the other hand the other connection target was not made intrinsically safe.

### Solution

#### Possibility 1

If the connection should be made intrinsically safe, make this setting for all the connection's targets. To do this, select the Intrinsically safe check box for each one in the Function data (logic) group box in the Properties <...> dialog. In the Connection point logic dialog, select the Intrinsic safety possible check box for each function connection.

#### Possibility 2

If the connection is not intended to be intrinsically safe, deselect the Intrinsically safe check box for each one under Function data (logic) in the Properties <...> dialog.

Refresh the connections and then start a new check run.