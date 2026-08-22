# CONNECTION_TERMINAL_CONNECTIONDESIGNATION(Int32) Property

CONNECTION\_TERMINAL\_CONNECTIONDESIGNATION(Int32) Property

Connection: Associated terminal connection point (connection point designation) # 31118. This property isn't indexed, and is read-only.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue CONNECTION_TERMINAL_CONNECTIONDESIGNATION( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ CONNECTION_TERMINAL_CONNECTIONDESIGNATION {
   PropertyValue^ get(int index);
   void set (int index, PropertyValue^ value);
}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

This property can be used in terminal diagrams in the data area of the cable chart (via the placeholder elements "Cable chart data area external" and "Cable chart data area internal"). Indicates the connection point designation of the terminal to which the connection is connected. Thus, you can see from the cable chart which connection is to be connected to which terminal connection point. For example, this is helpful if you use the placeholder elements "Target via connection point", "Connection via connection point" or "Connection / cable via connection point" to output several terminal connection points in a row.

See Also

#### Reference

[ConnectionPropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList.html)
  
[ConnectionPropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_TERMINAL_CONNECTIONDESIGNATION.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_TERMINAL_CONNECTIONDESIGNATION(Int32))