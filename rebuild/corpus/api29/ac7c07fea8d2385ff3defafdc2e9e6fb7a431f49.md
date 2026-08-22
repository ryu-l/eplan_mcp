# MDPropertyValue Class

MDPropertyValue Class

Class holding value of P8 Master Data property.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.MasterData.MDPropertyValue**

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
[DefaultMember("Item")]
public sealed class MDPropertyValue
```
```

```
```
[DefaultMember("Item")]
public ref class MDPropertyValue sealed
```
```

Remarks

MDPropertyValue object can be in one of three states: \* Created by user. This object is not connected with any property list or `object stored in master data database`. It is and off-line property. \* Collected from property list. It is an on-line property. \* Collected from any master data object. It is an on-line property. In two last cases overloads of the `PropertyValue::Set` method: **Eplan::EplApi::MDPropertyValue:**, **Eplan::EplApi::MDPropertyValue:**, **Eplan::EplApi::MDPropertyValue::Set(System:** etc, are setting values in original locations.

MDPropertyValue object can hold values of following types: \* int, \* string, \* double, \* bool, \* DateTime \* [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html), \* [Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html). Class implements conversion operators that will simplify access to P8 property values stored inside of MDPropertyList class object. User does not have to use this class explicitly, it allows to assign P8 property value in a simple way. See example. Value of the property can be changed using overloads of the `PropertyValue::Set` method: **Eplan::EplApi::MDPropertyValue:**, **Eplan::EplApi::MDPropertyValue:**, **Eplan::EplApi::MDPropertyValue::Set(System:** etc.

Example

Please note that following code:

- [C#](#i-tab-content-4662158a-6d9c-4002-a860-ad9b5ed04672)

```
MDPropertyValue oPv = oPart.Properties[Properties.MDPartsDatabaseItem.ARTICLE_DESCR1];
oPv = oPv + " additional comment";
//will create new off-line property value object and assign it into variable oPv.
```

- [C#](#i-tab-content-0dcbd1ce-f85b-4c54-bbe6-0e8f662738bd)

```
MDPart oPart = m_MDPartsDatabase.Parts[0]; //a valid master data part object

//here MDPropertyValue is implicit created from int constant ('5') and it is assigned to the property list.
oPart.Properties[Eplan.EplApi.MasterData.Properties.MDPartsDatabaseItem.ARTICLE_HEIGHT] = 5;

//here MDPropertyValue is implicit created from string constant ("7") and it is assigned to the property list.
oPart.Properties[Eplan.EplApi.MasterData.Properties.MDPartsDatabaseItem.ARTICLE_HEIGHT] = "7";

//here MDPropertyValue is read form property list and implicit converted to string.
string s = oPart.Properties[Eplan.EplApi.MasterData.Properties.MDPartsDatabaseItem.ARTICLE_HEIGHT];

//here MDPropertyValue is read form property list and implicit converted to int.
int i = oPart.Properties[Eplan.EplApi.MasterData.Properties.MDPartsDatabaseItem.ARTICLE_HEIGHT];
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [MDPropertyValue Constructor](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~_ctor().html) | Default constructor. Creates a MDPropertyValue object. |

[Top](#top)

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Definition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Definition.html) | Returns an object that provides information about the property and its definition. The information includes: name of the property, it's data type, whether it is indexed or not, whether it is read-only, upper/lower bounds of values for numerical properties. |
| Public Property | [Id](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Id.html) | Returns P8-Property descriptor ( id and index ) of the object. Off-line MDPropertyValue objects don't have descriptors because they point to value directly. off-line MDPropertyValue is created by operators that take base types values. |
| Public Property | [Indexes](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Indexes.html) | Returns array of indexes for which property value is not empty. It can be used with MDPropertyValue::operator []; |
| Public Property | [IsEmpty](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~IsEmpty.html) | Checks if property value is empty. If its not it can be read. IMPORTANT: If property is indexed you have to specify index. |
| Public Property | [Item](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Item.html) | Returns [MDPropertyValue](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue.html) object at specified index. |
| Public Property | [LastUsedIndex](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~LastUsedIndex.html) | Returns number of highest used index. Index value starts from 1. If it is not indexed-property or there index is not used, LastUsedIndex is 0; Object of MDPropertyValue have to point to on-line property. |
| Public Property | [Parent](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Parent.html) | Property list to which this property value is connected. |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Dispose().html) | Destructor for deterministic finalization of MDPropertyValue object. |
| Public Method | [GetDisplayString](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~GetDisplayString.html) | Display value of property as [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html). |
| Public Method | [Set](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Set.html) | Overloaded. Sets [System.DateTime](#) value in MDPropertyValue object. |
| Public Method | [ToBool](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~ToBool.html) | Converts this MDPropertyValue object to `System::Boolean`. |
| Public Method | [ToDouble](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~ToDouble.html) | Converts this MDPropertyValue object to `doule`. |
| Public Method | [ToInt](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~ToInt.html) | Converts this MDPropertyValue object to `long`. |
| Public Method | [ToMultiLangString](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~ToMultiLangString.html) | Converts this MDPropertyValue object to [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html). |
| Public Method | [ToPointD](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~ToPointD.html) | Conversion this MDPropertyValue object to [Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html). |
| Public Method | [ToString](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~ToString.html) | Overloaded. Returns string value of this property. When type of property is MultiLangString then only specified language is returned. In case of off-line MDPropertyValue object, stored value is returned without any cast. When property can not be read, `default_value` is returned instead of throwing `MDEmptyPropertyException` . |
| Public Method | [ToTime](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~ToTime.html) | Converts this MDPropertyValue object to `System::DateTime`. |

[Top](#top)

Public Operators

|  |  |
| --- | --- |
| public Operator [Implicit Type Conversion](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~op_Implicit.html) | Overloaded. Converts MDPropertyValue object to `long`. |

[Top](#top)

See Also

#### Reference

[MDPropertyValue Members](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue_members.html)
  
[Eplan.EplApi.MasterData Namespace](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData_namespace.html)
  
[PropertiesAndHandleObjectPropertyList Class](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObjectPropertyList.html)
  
[MDPartsDatabaseItemPropertyList Class](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue)