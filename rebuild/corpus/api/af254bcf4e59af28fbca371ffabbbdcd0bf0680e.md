# CutOff(PointD) Method

CutOff(PointD) Method

Cut off objects at a given position, from page currently opened in graphical editor.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public GraphicalPlacement[] CutOff( 
   PointD oPoint
)
```
```

```
```
public:
array<GraphicalPlacement^>^ CutOff( 
   PointD oPoint
)
```
```

#### Parameters

*oPoint*
:   Point of object to cut off.

#### Return Value

Modified graphical objects, empty array if it was last object, NULL if nothing was removed.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Is thrown when there is no page currently opened in graphical editor. |
| [System.ArgumentNullException](#) | Is thrown in case of NULL parameters. |

See Also

#### Reference

[Edit Class](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit.html)
  
[Edit Members](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit_members.html)
  
[Overload List](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~CutOff.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)