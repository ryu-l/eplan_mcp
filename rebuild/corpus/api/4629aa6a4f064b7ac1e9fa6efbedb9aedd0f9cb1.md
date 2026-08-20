# DESIGNATION_SUBPLACEOFINSTALLATION6 Property

DESIGNATION\_SUBPLACEOFINSTALLATION6 Property

Installation site (sub-identifier 6) # 1406.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue DESIGNATION_SUBPLACEOFINSTALLATION6 {get; set;}
```
```

```
```
public:
property PropertyValue^ DESIGNATION_SUBPLACEOFINSTALLATION6 {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

This property is used as part of a name. In order to set it, member `NameParts` must be used on object which name will be changed. Additionally for setting this property on a Page object, a function Page::SetName() or the Page constructor can be used.

See Also

#### Reference

[PlanningSegmentPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList.html)
  
[PlanningSegmentPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList_members.html)
  
[Overload List](topic2182.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)