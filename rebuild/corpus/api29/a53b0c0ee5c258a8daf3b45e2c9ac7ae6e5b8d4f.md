# WindowMacro(WindowMacro,Int32,PointMate,Mate,Double,Double,Double,Double,NumerationMode) Method

WindowMacro(WindowMacro,Int32,PointMate,Mate,Double,Double,Double,Double,NumerationMode) Method

Places a window macro with snapping source mate to a target mate from another object.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public Placement3D[] WindowMacro( 
   WindowMacro oMacro,
   int nVariant,
   PointMate oSourceMate,
   Mate oTargetMate,
   double dRotationAngle,
   double dX,
   double dY,
   double dZ,
   WindowMacro.Enums.NumerationMode nNumerationMode
)
```
```

```
```
public:
array<Placement3D^>^ WindowMacro( 
   WindowMacro^ oMacro,
   int nVariant,
   PointMate^ oSourceMate,
   Mate^ oTargetMate,
   double dRotationAngle,
   double dX,
   double dY,
   double dZ,
   WindowMacro.Enums.NumerationMode nNumerationMode
)
```
```

#### Parameters

*oMacro*
:   Object with opened macro.

*nVariant*
:   Index of the macro variant to be placed (0 based).

*oSourceMate*
:   Given mate of a macro

*oTargetMate*
:   Target mate

*dRotationAngle*
:   Additional rotation angle (radian)

*dX*
:   Additional offset in x direction

*dY*
:   Additional offset in y direction

*dZ*
:   Additional offset in z direction

*nNumerationMode*
:   Numeration mode

#### Return Value

Inserted placements

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters.. |
| **ArgumentNullException** | Null was set to a parameter. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during inserting the macro. Please refer to the error message. |

Remarks

The position and/or orientation of the associated placements changes after the snapping, in a way that the macro's source mate in the same position as a target mate.

See Also

#### Reference

[Insert3D Class](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert3D.html)
  
[Insert3D Members](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert3D_members.html)
  
[Overload List](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert3D~WindowMacro.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert3D~WindowMacro(WindowMacro,Int32,PointMate,Mate,Double,Double,Double,Double,NumerationMode))