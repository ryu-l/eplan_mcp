# FUNC_DEVICETYPE_MANUAL Property

FUNC\_DEVICETYPE\_MANUAL Property

Device group # 20294.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_DEVICETYPE_MANUAL {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_DEVICETYPE_MANUAL {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.Int64.

Remarks

Manual assignment of the function to a device group (which determines the DT format). Using this property, you can select another DT format for specific functions, e.g., a connection can then have a different DT format than a cable. If the property is empty, the device group will be derived automatically from the function definition.

See Also

#### Reference

[Placement3DPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html)
  
[Placement3DPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_DEVICETYPE_MANUAL.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)