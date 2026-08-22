# Data backup strategies

Backing up resource folder via a compression program:

The resource folder can be backed up using a compression program, for example, 7-ZIP (see [Backing up the resource folder](admin_h_backup_resourcefolder.htm)). By assigning the proper names to the zipped files, the backed-up files can be allocated easily.

Benefit: Compression can be automated, and does not require any further intervention on the userâs part.

Drawback: All resources are always compressed, which creates redundant data collections.

Differential backup of the resource folder:

Initially, all resources are backed up onto an external storage medium. Then, all changes since that backup are stored.

Benefit: Can be automated, and does not require any further intervention on the userâs part. To restore the files, only the full backup and the most recent differential backup will be required.

Drawback: Higher memory usage than with incremental backups

Incremental backup of the resource folder:

Initially, all resources are backed up onto an external storage medium. Then, only the changes since the last backup are stored. Each time, a new folder is created so as to have a transparent chronology.

Benefit: Can be automated, and does not require any further intervention on the userâs part. Low memory usage; if necessary, the data can be compressed on a backup medium. No redundant data.

Drawback: More effort in restoring files than with differential backups.

Exporting user preferences:

User preferences are exported to an .epf file via the export function of the user interface. The process can be automated by means of a script. If named accordingly, the .epf file can be identified easily.

Exporting the information model:

The information model is exported to an .eox file via the export function of the user interface. The process can be automated by means of a script. If named accordingly, the .eox file can be identified easily.