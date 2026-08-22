# WriteProtected Property (InterruptionPoint)

WriteProtected Property (InterruptionPoint)

Check if object is currently write protected or sets Manual write protection

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual bool WriteProtected {get; set;}
```
```

```
```
public:
virtual property bool WriteProtected {
   bool get();
   void set (    bool value);
}
```
```

#### Property Value

true : if object is currently write-protected

false : if no write protection was set or if write protection was disabled

Exceptions

| Exception | Description |
| --- | --- |
| [WriteProtectionChangeNotAllowed](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.WriteProtectionChangeNotAllowed.html) | Thrown if because of current write protection state, no further modifications are allowed. |

See Also

#### Reference

[InterruptionPoint Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPoint.html)
  
[InterruptionPoint Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPoint_members.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPoint~WriteProtected)