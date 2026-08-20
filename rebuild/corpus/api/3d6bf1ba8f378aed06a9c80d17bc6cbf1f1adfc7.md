# RouteConnection Method

RouteConnection Method

Creates new route of an existing connection 3d.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public RoutingSegment[] RouteConnection( 
   Connection3D connection3D,
   RoutingSegment[] preRoutingSegments
)
```
```

```
```
public:
array<RoutingSegment^>^ RouteConnection( 
   Connection3D^ connection3D,
   array<RoutingSegment^>^ preRoutingSegments
)
```
```

#### Parameters

*connection3D*
:   Connection3D being routed

*preRoutingSegments*
:   Pre-set array of segments

#### Return Value

An array of routed segments.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when necessary argument is `null`. |
| [System.ApplicationException](#) | An interface used for export could not be created. |

See Also

#### Reference

[ConnectionService3D Class](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService3D.html)
  
[ConnectionService3D Members](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService3D_members.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)