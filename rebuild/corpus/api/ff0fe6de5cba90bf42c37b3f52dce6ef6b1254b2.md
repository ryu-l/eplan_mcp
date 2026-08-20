# GetTemplatesFromDeviceList Method

GetTemplatesFromDeviceList Method

This method returns an array of DeviceService::TemplatesInfo containing information about function templates associated with specific part numbers existing in the device list of the given project.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public DeviceService.TemplatesInfo[] GetTemplatesFromDeviceList( 
   Project oProject
)
```
```

```
```
public:
array<DeviceService.TemplatesInfo^>^ GetTemplatesFromDeviceList( 
   Project^ oProject
)
```
```

#### Parameters

*oProject*
:   Project from which the device list will be searched.

#### Return Value

An array of DeviceService::TemplatesInfo objects containing information about function templates associated with specific part numbers.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ArgumentNullException** | Null was passed to a parameter. |

See Also

#### Reference

[DeviceService Class](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService.html)
  
[DeviceService Members](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService_members.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)