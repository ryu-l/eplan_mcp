# Action: XPrjActionUpgradeProjects

|  |  |
| --- | --- |
| **Parameters** | **Description** |
| Project | Project name with complete file path. |
| Folder | Folder whose [projects](Glossary_o_projekte.htm) are to be updated. Subfolders of the specified folder are included. |
| Archive | 1: zw1 projects are also updated and then zipped. |
| BaseProject | 1: zw9 and zx1 projects are also updated and then zipped. |
| UpgradeWriteProtectedProjects | 1: Write-protected projects (file name extensions \*.elr and \*.elt, \*.els, \*.elx) are also updated. |
| UpgradeXMLProjects | 1: Projects / [basic projects](Glossary_o_basisprojekte.htm) in XML format (\*.ept and \*.epj, \*.zx2) are also updated. |
| FileTypes | All the projects are updated (corresponds to the setting \*.\*). |
| PackOriginalProject | 1: The original projects are zipped after updating into a 7zip file (default setting). |
| UpdateConnections | 1: The [connections](Glossary_o_verbindungen.htm) are updated in the project (default setting = 0). |
| NoBackup | 1: No backup copy of the old version is created (default setting = 0). |
| IgnoreUpgradeBackups | 1: Backup projects are ignored when a complete folder is converted (default setting = 0). The backup projects have names that follow the following pattern: [PROJECT\_NAME]\_V[Version]\_[Backup\_time]. |

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example:](javascript:void(0);)

```
XPrjActionUpgradeProjects 
/Project:$(MD_PROJECTS)ESS_Sample_Project.elk
```