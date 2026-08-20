# PrjMessagesRegisteredCollection Constructor(Boolean,Project)

PrjMessagesRegisteredCollection Constructor(Boolean,Project)

Constructor. initializes the matching enumerator.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PrjMessagesRegisteredCollection( 
   bool bOnlyLicensed,
   Project oProject
)
```
```

```
```
public:
PrjMessagesRegisteredCollection( 
   bool bOnlyLicensed,
   Project^ oProject
)
```
```

#### Parameters

*bOnlyLicensed*
:   If set to true only messages that are licensed in the actual system will be regarded

*oProject*
:   Properties of ElectroMessage will be set/get to/from this Project. Can't be null.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Null Project was passed to a parameter. |
| [System.ArgumentException](#) | Invalid Project was passed to a parameter. |

See Also

#### Reference

[PrjMessagesRegisteredCollection Class](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesRegisteredCollection.html)
  
[PrjMessagesRegisteredCollection Members](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesRegisteredCollection_members.html)
  
[Overload List](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesRegisteredCollection~_ctor.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)