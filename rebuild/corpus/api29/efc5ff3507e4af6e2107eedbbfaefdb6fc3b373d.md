# XGedIaFormatSymbol

XGedIaFormatSymbol

formats all property- texts of a symbol reference can be offered for configurable toolbar

| Parameter | Description |
| --- | --- |
| language | ``` language (AllLanguagesColumn, AllLanguagesRow, OneLanguageVariable, de_DE, en_US ...) ``` |
| height | ``` text height (Value in mm or In or "-16002" for "from layer") ``` |
| color | ``` text color (0=black, 1=red, 2=yellow, 3=green, 4=cyan, 5=blue, 6=magenta, 7=black,                                  8=white, 9=light gray, 252=dark gray, 253=gray, -16002=from layer;                      The user can set other values in the color selection; possible values are from 0 to 256. ``` |
| justification | ``` adjustment (1=kTopLeft, 2=kTopCenter, 3=kTopRight, 4=kMiddleLeft, 5=kMiddleCenter,                                          6=kMiddleRight, 7=kBottomLeft, 8=kBottomCenter, 9 = kBottomRight,                                          10=kBaseLineLeft, 11=kBaseLineCenter, 12=kBaseLineRight,                                          13=kSpecialLeft (Special Attachment-Types for PathTexts in DIN- and USA-Project),                                          14=kSpecialCenter (should not be used in new projects, just to be compatible to E5),                                          15=kSpecialRight, 16=kJicSpecialLeft (Special Attachment-Types for PathTexts in JIC-Project),                                          17=kJicSpecialCenter(should not be used in new projects, just to be compatible to E5),                                          18 = kJicSpecialRight) ``` |
| angle | ``` angle to the X-axis in ° (0°,45°, 90°, 135°, 180°, -45°, -90°, -135°) ``` |
| font | ``` text font (0=font 1 of company settings, 1=font 2 of company settings, ..., 9=font 10 of company settings) ``` |
| visible | ``` text visibility (0=invisible, 1=visible, 2=from layer) ``` |
| bold | ``` text accentuation (0=normal, 1=bold) ``` |
| italic | ``` text accentuation (0=normal, 1=italic) ``` |
| underline | ``` text accentuation (0=normal, 1=underlined) ``` |
| showtextbox | ``` Use Text box? (0=no text box, 1=rectangular text box, 2=elliptic text box, 3=from layer) ``` |
| setframeactive | ``` Frame active? (0=should not be active, 1=should be active) ``` |
| showframe | ``` Frame shown? (0=no alignment box, 1=show alignment box) ``` |
| framewidth | ``` frame width in mm or In ``` |
| frameheight | ``` frame height in mm or In ``` |
| adjustframe | ``` Adjust Frame? (1 = do not fit in, 16 = Text: Width fixed - never word-wrap, 32 = Text: Height fixed - never word-wrap,                                                                                         64 = Text: word-wrap,                                           80 = Text: Width fixed - word-wrap,                                                                                         128 = Text: remove line breaks,                                           144 = Text: Width fixed - never word-wrap - remove line breaks,                                           208 = Text: Width fixed - word-wrap - remove line breaks) ``` |
| propertyId | ``` ID (of 5 digits) of a property of the symbol; if this ID is set, only this property-text will be changed ``` |
| propertyIndex | ``` index of the property ID, negative values are possible (example: ... -1, 1, 2, 3, ...) ``` |
| linespacing | ``` Row spacing in number of lines. Please use value -160.02 to set 'From layer' ``` |
| paragraphspacing | ``` paragraph spacing in mm or In ``` |
| layer | ``` layer name (example: "EPLAN501") ``` |

Remarks

```
 In properties which should not be changed, leave simply question mark ("?").
```

```
 The settings are the same as in the characteristic text dialog.
```

Example

```
 See
```

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: XGedIaFormatSymbol)