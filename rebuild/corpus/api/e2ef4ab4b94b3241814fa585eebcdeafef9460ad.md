# Create(Page) Method

Create(Page) Method

This method should never be used. Always throws NotImplementedException. DimensionCircle cannot be created without circle.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void Create( 
   Page page
)
```
```

```
```
public:
void Create( 
   Page^ page
)
```
```

#### Parameters

*page*
:   The [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) the circle will be placed on

Exceptions

| Exception | Description |
| --- | --- |
| [System.NotImplementedException](#) | Always thrown. |
| [Eplan.EplApi.DataModel.InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when the given [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) has the PageType set to ExternalDocument. |

See Also

#### Reference

[DimensionCircle Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionCircle.html)
  
[DimensionCircle Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionCircle_members.html)
  
[Overload List](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionCircle~Create.html)
  
[Page Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)