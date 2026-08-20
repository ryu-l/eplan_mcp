# FRAME_DEVTAGSEARCHDIR_FOR_GOST Property

FRAME\_DEVTAGSEARCHDIR\_FOR\_GOST Property

DT adoption: Search direction conforming to GOST standard # 12104.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FRAME_DEVTAGSEARCHDIR_FOR_GOST {get; set;}
```
```

```
```
public:
property PropertyValue^ FRAME_DEVTAGSEARCHDIR_FOR_GOST {
   PropertyValue^ get();
   void set (    PropertyValue^ value);
}
```
```

#### Property Value

Returns property value of type System.Boolean.

Remarks

This plot frame property allows the search direction for DT adoption to be changed to suit the GOST standard. If this property is activated, then in plot frames with a "Vertical" report generation direction, the DT is searched for towards the right and with a "Horizontal" report generation direction the DT is searched for downwards.

See Also

#### Reference

[PlotFramePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList.html)
  
[PlotFramePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList~FRAME_DEVTAGSEARCHDIR_FOR_GOST.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)