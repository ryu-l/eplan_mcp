# Dialog Publish

[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Dialog call:](javascript:void(0);)

You have opened a project. Select the menu [items](Glossary_o_bauteile.htm) Project > Publish.

In this dialog, you can specify the [settings](Glossary_o_einstellungen.htm) for the export of a project to the EPDZ format. The EPDZ format can be read via the dropbox on mobile [devices](Glossary_o_betriebsmittel.htm) (for example iPad) by means of the EPLAN View App. The EPDZ file contains the [project properties](Glossary_o_projekteigenschaften.htm), page [properties](Glossary_o_eigenschaften.htm), and [layout space](Glossary_o_bauraum.htm) properties, and thus also the complete [project structure](Glossary_o_projektstruktur.htm). In addition, the EPDZ file contains for each project page an SVG file with the 2D vector graphic, and for each layout space an E3D file with the 3D graphical data.

![](../Pictures/Gui/ALL/note.png)Note:

The function for exporting a project into an EPDZ file [for usage in EPLAN Smart Wiring](productionwiringgui_h_smartwiringdatenexportieren.htm) is located under the menu items Utilities > Manufacturing data > EPLAN Smart Wiring.

Overview of the main dialog elements:

Source (page / 3D model):

This field displays the project name of the project to be exported. The entry in this field cannot be edited.

Scheme:

Select a scheme that contains the settings for the EPDZ export from the drop-down list.

The [...] button opens the dialog Settings: Publish. In this dialog you define the settings for exporting EPDZ files and save them as a scheme.

EPDZ file:

Name of the file to which the opened project is to be exported. By default, the project name is entered with the file extension "epdz".

You can use the [...] button to assign a file name or select the name of an existing file.

---

Group box Export medium

Storage medium:

If this export medium is selected, the EPDZ file is output to a storage medium. When publishing to storage media, you can save the EPDZ file to a USB device, or burn it directly to a CD / DVD.  
  
The storage location can be entered in the Output directory field.

The [...] button opens the Select directory dialog in order to select any directory of your choice for the export.

E-mail:

If this export medium is selected, the EPDZ file is sent as an e-mail. When publishing as an e-mail, you can send the EPDZ file directly to the mobile device.

![](../Pictures/Gui/ALL/note.png)Note:

Mobile devices cannot read split files. This is why the file cannot be split into several, smaller parts when sending an EPDZ file by e-mail.

See also

[Publishing Projects](projects_h_veroeffentlichen.htm)

[Dialog Settings: Publish](edaexportgui_d_einstellungenveroeffentlichen.htm)