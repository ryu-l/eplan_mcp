# Property(PlotFrame,Int32) Property

Property(PlotFrame,Int32) Property

Method used by operator[] in order to access indexed properties.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public new PropertyValue Property( 
   Properties.PlotFrame id,
   int index
) {get; set;}
```
```

```
```
public:
new property PropertyValue^ Property {
   PropertyValue^ get(Properties.PlotFrame id, int index);
   void set (Properties.PlotFrame id, int index, PropertyValue^ value);
}
```
```

#### Parameters

*id*
:   Identifier of the PlotFrame's property

*index*
:   Index of the PlotFrame's property

#### Property Value

[Eplan.EplApi.DataModel.PropertyValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html) object that automaticaly converts into common used types.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an external error. Please refer to the exception message. |
| [Eplan.EplApi.DataModel.PropertyNotFoundException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyNotFoundException.html) | PropertyNotFoundException |
| [Eplan.EplApi.DataModel.InvalidIndexException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidIndexException.html) | InvalidIndexException |
| [Eplan.EplApi.DataModel.PropertyReadOnlyException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyReadOnlyException.html) | PropertyReadOnlyException |
| [Eplan.EplApi.DataModel.SettingValueFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SettingValueFailedException.html) | SettingValueFailedException |

See Also

#### Reference

[PlotFramePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList.html)
  
[PlotFramePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList~Property.html)
  
[PropertyValue Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html)
  
[Properties.PlotFrame Enumeration](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Properties+PlotFrame.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList~Property(PlotFrame,Int32))