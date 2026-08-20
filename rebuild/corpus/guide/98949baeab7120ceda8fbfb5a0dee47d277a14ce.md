# Exporting Missing-word List

You can export project texts that Eplan couldn't translate as missing-word lists. These project texts can then be translated into one or more languages outside of Eplan and reimported.

Preconditions:

- You have opened a project.
- You have defined a dictionary.

### Determine translation segments, source language, and target language

Before generating a missing-word list, you can specify how the project texts are to be broken down into translation segments. A translation segment can be a word, a sentence or the entire entry.

1. Select the following commands: File > Settings > Projects > "Project name" > Translation > General.
2. In order to export a translation segment for every sentence select the "Sentence" entry from the Segment drop-down list.
3. In order to export a translation segment for the entire entry of a text box, select the "Entire entry" entry from the Segment drop-down list.
4. Select an entry from the Source language drop-down list. The source language here is the language for which you already have translation text.
5. Check whether the desired target languages are listed as the translation languages in the Translation group box in the Languages field.
6. If the languages are not present, click ![](../Pictures/Gui/ALL/all_new_as.png) (New), and select the desired languages.
7. Click [OK].

### Export target languages

The target languages are the languages for which you have no translation text. The missing-word list can be exported for one or more target languages.

1. To export a missing-word list for the entire project, select the project name or the desired pages in the page navigator.
2. To export a missing-word list for individual, translatable schematic elements, double-click a page, and select the desired schematic elements in the graphical editor.
3. Select the following commands: Tab Tools > Command group Translation > Export missing-word list.
4. In the Export missing-word list dialog, select the storage location as well as a file type and enter a file name.

   ![](../Pictures/Gui/ALL/note.png)Note:

   The entries displayed under File type have the following significance:  
   XML file (\*.etd): This format is used for the Eplan P8-internal data exchange.
     
   Tab-delimited Unicode file (\*.txt): This format is used for the "external" data exchange, e.g., with Excel.
5. Confirm your entries.
6. Select all the desired target languages in the Select languages dialog.
7. Click [OK].

See also

[The Dictionary](translatedbgui_k_start.htm)

[Structure of Keywords](translatedbgui_k_eingabemoeglichkeit.htm)

[Importing a Missing-word List](translategui_h_fehlwortimport.htm)