# FindNameGivingObject(Page,Function) Method

FindNameGivingObject(Page,Function) Method

Finds an object, that would give the f function its name, if f has no its instance name parts assigned (has no visible device tag). Returns NULL, if no such object exists or f don't take over a name.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public FunctionBase FindNameGivingObject( 
   Page page,
   Function f
)
```
```

```
```
public:
FunctionBase^ FindNameGivingObject( 
   Page^ page,
   Function^ f
)
```
```

#### Parameters

*page*
:   A page to search the result object on.

*f*
:   Function, which takes over a name.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |

Remarks

Similar to the FindNameGivingFunction method but returns objects like e.g. LocationBox too.

See Also

#### Reference

[NameService Class](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService.html)
  
[NameService Members](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService_members.html)
  
[Overload List](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~FindNameGivingObject.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~FindNameGivingObject(Page,Function))