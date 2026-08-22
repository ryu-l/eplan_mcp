# Renumber.Enums.MultipleTerminals Enumeration

Renumber.Enums.MultipleTerminals Enumeration

Parameter enum for numbering terminals with "Allow same designations" property .

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public enum Renumber.Enums.MultipleTerminals : System.Enum
```
```

```
```
public enum class Renumber.Enums.MultipleTerminals : public System.Enum
```
```

Members

| Member | Value | Description |
| --- | --- | --- |
| **DontModify** | 0 | Terminals with the property "Allow same designations" are ignored during numbering. |
| **NumberIndividually** | 2 | Terminals with the "Allow same designations" property are each given their own number. Therefore, multiple terminals which had the same number before numbering will have different numbers after numbering. |
| **NumberSame** | 1 | Terminals with the same designation with the "Allow same designations" property are given the same number. |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.HEServices.Renumber.Enums.MultipleTerminals**

See Also

#### Reference

[Eplan.EplApi.HEServices Namespace](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices_namespace.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Renumber+Enums+MultipleTerminals)