# DESIGNATION_SUBPLANT9 Property

DESIGNATION\_SUBPLANT9 Property

Function designation (sub-identifier 9) # 1109.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue DESIGNATION_SUBPLANT9 {get; set;}
```
```

```
```
public:
property PropertyValue^ DESIGNATION_SUBPLANT9 {
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

[FunctionBasePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList.html)
  
[FunctionBasePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList~DESIGNATION_SUBPLANT9.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)