# SetPages Method

SetPages Method

Sets page names.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool SetPages( 
   string strFullLinkFileName,
   string[] lPages
)
```
```

```
```
public:
bool SetPages( 
   String^ strFullLinkFileName,
   array<String^>^ lPages
)
```
```

#### Parameters

*strFullLinkFileName*
:   Full link file name of the project.

*lPages*
:   Table with page names.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if null was passed as an argument. |

See Also

#### Reference

[MRUList Class](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.MRUList.html)
  
[MRUList Members](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.MRUList_members.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)