# ImportDeviceList(Project,String,Format) Method

ImportDeviceList(Project,String,Format) Method

This function imports a device list into a given project.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void ImportDeviceList( 
   Project oProject,
   string strImportFilePath,
   DeviceService.Format fileFormat
)
```
```

```
```
public:
void ImportDeviceList( 
   Project^ oProject,
   String^ strImportFilePath,
   DeviceService.Format fileFormat
)
```
```

#### Parameters

*oProject*
:   Project into which the device list will be imported.

*strImportFilePath*
:   Full file name of the device list file to import.

*fileFormat*
:   Format of the import file\: By default the following file formats are available\: XML or CSV. The enum Format defines the available values. If an invalid format is set, the file is expected to be XML.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ArgumentNullException** | Null was passed to a parameter. |
| **ApplicationException** | The internal interface for importing a device list could not be created. |
| **BaseException** | An error occurred during the import of a device list. Please refer to the exception message. |
| **Eplan.EplApi.HEServices.Exceptions.InvalidConverter** | Thrown when given parameter  `fileFormat`  isn't valid converter or such conversion dosesn't exist at all. |

See Also

#### Reference

[DeviceService Class](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService.html)
  
[DeviceService Members](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService_members.html)
  
[Overload List](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~ImportDeviceList.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~ImportDeviceList(Project,String,Format))