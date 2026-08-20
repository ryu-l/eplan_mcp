# ProductGroup Property

ProductGroup Property

Gets/Sets the product group of the part.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual MDPartsDatabaseItem.Enums.ProductGroup ProductGroup {get; set;}
```
```

```
```
public:
virtual property MDPartsDatabaseItem.Enums.ProductGroup ProductGroup {
   MDPartsDatabaseItem.Enums.ProductGroup get();
   void set (    MDPartsDatabaseItem.Enums.ProductGroup value);
}
```
```

#### Property Value

Product group of the part.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown if cannot set given ProductGroup for the current GenericProductGroup of the part. |

See Also

#### Reference

[MDPart Class](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart.html)
  
[MDPart Members](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart_members.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)