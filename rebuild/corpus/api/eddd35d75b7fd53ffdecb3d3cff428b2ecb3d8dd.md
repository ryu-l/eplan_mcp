# DeleteDeviceList(String) Method

DeleteDeviceList(String) Method

This function deletes the device list in the given project.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void DeleteDeviceList( 
   string strFullLinkFileName
)
```
```

```
```
public:
void DeleteDeviceList( 
   String^ strFullLinkFileName
)
```
```

#### Parameters

*strFullLinkFileName*
:   Full link file name of the project in which the device list will be deleted.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | null was passed to a parameter. |
| **ApplicationException** | The internal interface for deleting device lists could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred while deleting the device list. Please refer to the exception message. |

See Also

#### Reference

[DeviceService Class](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService.html)
  
[DeviceService Members](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService_members.html)
  
[Overload List](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~DeleteDeviceList.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)