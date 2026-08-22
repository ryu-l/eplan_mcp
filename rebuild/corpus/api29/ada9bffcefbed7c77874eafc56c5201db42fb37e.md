# VerifyMDPartsDatabaseItems(Project,IEnumerable<MDPartsDatabaseItem>) Method

VerifyMDPartsDatabaseItems(Project,IEnumerable<MDPartsDatabaseItem>) Method

Starts a check run for the given MDPartsDatabaseItems (MDParts).

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void VerifyMDPartsDatabaseItems( 
   Project oProject,
   IEnumerable<MDPartsDatabaseItem> oItems
)
```
```

```
```
public:
void VerifyMDPartsDatabaseItems( 
   Project^ oProject,
   IEnumerable<MDPartsDatabaseItem^>^ oItems
)
```
```

#### Parameters

*oProject*
:   Project to write messages to.

*oItems*
:   Parts collection.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Throw if parameter is invalid. |

Remarks

Last-used scheme will be used which is currently set in GUI.

See Also

#### Reference

[Check Class](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check.html)
  
[Check Members](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check_members.html)
  
[Overload List](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyMDPartsDatabaseItems.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyMDPartsDatabaseItems(Project,IEnumerable{MDPartsDatabaseItem}))