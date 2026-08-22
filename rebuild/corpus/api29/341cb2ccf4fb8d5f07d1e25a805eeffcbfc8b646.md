# Properties Property

Properties Property

Property enabling access to internal properties of the Page object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public new PagePropertyList Properties {get;}
```
```

```
```
public:
new property PagePropertyList^ Properties {
   PagePropertyList^ get();
}
```
```

#### Property Value

Eplan properties of the page.

Exceptions

| Exception | Description |
| --- | --- |
| [InsufficientLicenceException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InsufficientLicenceException.html) | Thrown when no new logical page can be added to the project. |

Example

- [C#](#i-tab-content-d63e7a89-6aee-4866-be1a-6b09c8a3d5ea)

```
Page page = oProject.Pages[10];
page.Properties.PAGE_REVISION_APPROVEDBY = "John";
string strCounter = page.Properties.PAGE_COUNTER;
```

See Also

#### Reference

[Page Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)
  
[Page Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page_members.html)
  
[PagePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList.html)
  
[Page Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Page.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~Properties())