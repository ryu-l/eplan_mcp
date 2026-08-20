# GetPartsWithFilterScheme Method

GetPartsWithFilterScheme Method

Gets parts using the filter from GUI.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public MDPart[] GetPartsWithFilterScheme( 
   string strGUIFilter
)
```
```

```
```
public:
array<MDPart^>^ GetPartsWithFilterScheme( 
   String^ strGUIFilter
)
```
```

#### Parameters

*strGUIFilter*
:   Filter scheme that is visible in window 'Parts management'

Remarks

If scheme-name is empty, the current filter scheme will be used (excluding 'no-filter' scheme). If scheme-name is null, the method returns elements that are visible if no filter scheme is used.

See Also

#### Reference

[MDPartsDatabase Class](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase.html)
  
[MDPartsDatabase Members](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase_members.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)