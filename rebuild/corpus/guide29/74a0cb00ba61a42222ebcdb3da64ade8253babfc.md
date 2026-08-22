# P024007: Main function with undefined trade

### Cause

The value "Property Fluid power (undefined)" was selected at the main function of the fluid device for the Trade property.

### Solution

1. Locate the fluid device in the schematic using the Go to (graphic) function from the popup menu in the Message management dialog.
2. Assign a defined trade to the main function.
3. Use the right media code in accordance with DIN ISO 1219-2 for the respective trade at the device tag of the main function.
4. Then start a new check run.