# P026072: No wire fabrication: <x>

### Cause

During the export of the wire fabrication data, a missing and / or incorrect setting was determined.

The placeholder <x> in the message specifies which setting is missing or which setting's value is too high. The following placeholders are possible:

- Missing cross-section
- Missing connection color
- Komax data for wire could not be determined
- Missing length
- Machine command target unknown
- Machine command source unknown
- Maximum cross-section exceeded
- Minimum cross-section underpassed
- Maximum length exceeded
- Machine data for wire could not be determined
- Bundle split - number of wires too high
- Wire termination processing target missing
- Wire termination processing source missing.

### Solution

1. Complete and / or correct the setting for the export of the wire fabrication data according to the placeholder text.
2. Export the data again.

![](../Pictures/Gui/ALL/note.png)Note:

Using a new check run (any desired scheme) this module-specific message can be deleted from the message management dialog.