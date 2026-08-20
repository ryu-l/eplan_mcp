# FUNC_ARTICLE_USED_SAFETYRELATEDVALUE(Int32) Property

FUNC\_ARTICLE\_USED\_SAFETYRELATEDVALUE(Int32) Property

Safety-related values: Use case in use # 20307.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public PropertyValue FUNC_ARTICLE_USED_SAFETYRELATEDVALUE( 
   int index
) {get; set;}
```
```

```
```
public:
property PropertyValue^ FUNC_ARTICLE_USED_SAFETYRELATEDVALUE {
   PropertyValue^ get(int index);
   void set (int index, PropertyValue^ value);
}
```
```

#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Indicates the use case that is used for the safety-related values of a part.

See Also

#### Reference

[SegmentTemplatePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList.html)
  
[SegmentTemplatePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList_members.html)
  
[Overload List](topic2423.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)