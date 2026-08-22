# PlantDesignationNumbersOnly Property

PlantDesignationNumbersOnly Property

Representation of XDtcDeviceTagCheck.Hierarchy.PlantDesignationNumbersOnly setting value. In P8-GUI it can be found in the menu:Options/Settings:Projects/<project>/Devices/DT syntax check:Structure identifier/Valid special characters. When this option is enabled (has `true` value) only numbers can be used in DeviceTag syntax. To make it work [EnableSyntaxCheck](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~EnableSyntaxCheck.html) must be `true`.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool PlantDesignationNumbersOnly {get; set;}
```
```

```
```
public:
property bool PlantDesignationNumbersOnly {
   bool get();
   void set (    bool value);
}
```
```

Remarks

This property might throw this same exceptions what functions **Eplan::EplApi::DataModel::ProjectSettings:** and **Eplan::EplApi::DataModel::ProjectSettings:** might throw.

See Also

#### Reference

[Project.DeviceTagSettings Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings.html)
  
[Project.DeviceTagSettings Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings_members.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+DeviceTagSettings~PlantDesignationNumbersOnly)