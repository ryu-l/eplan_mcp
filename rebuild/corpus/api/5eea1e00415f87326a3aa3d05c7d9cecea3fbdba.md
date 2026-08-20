# Set(String,ParserParameter) Method

Set(String,ParserParameter) Method

The start of any parse. Set the text to parse and fill the unit of this text in the parser parameters.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void Set( 
   string strValueToParse,
   ParserParameter parameter
)
```
```

```
```
public:
void Set( 
   String^ strValueToParse,
   ParserParameter^ parameter
)
```
```

#### Parameters

*strValueToParse*
:   the string with a number and optional a unit

*parameter*
:   the parameters with the unit of this string. Afterwards the unit group is defined for the unit parser.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | The value of the parameter object is NULL. |

See Also

#### Reference

[UnitParser Class](Eplan.EplApi.Baseu~Eplan.EplApi.Base.UnitParser.html)
  
[UnitParser Members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.UnitParser_members.html)
  
[Overload List](Eplan.EplApi.Baseu~Eplan.EplApi.Base.UnitParser~Set.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)