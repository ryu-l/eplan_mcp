# ARTICLE_ERPNR Property (MergedArticleReferencePropertyList)

ARTICLE\_ERPNR Property (MergedArticleReferencePropertyList)

ERP number # 22056. This property isn't indexed.

Overload List

| Overload | Description |
| --- | --- |
| [ARTICLE\_ERPNR(Int32)](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLE_ERPNR(Int32).html) | ERP number # 22056. This property isn't indexed. |
| [ARTICLE\_ERPNR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLE_ERPNR().html) | ERP number # 22056. |

Remarks

Unique part number in an external ERP system. ERP numbers may be up to 255 characters in length.

EPLAN reads article reference properties from function or if corresponding propoerty does not exists on function or is empty, then it is taken directly from the article. User needs to remember that setting values which removes property value for article reference property causes that they are read from article. Here is list of such values for each type: LONG - 0, STRING - empty string, BOOL - false, DOUBLE - 0.0 and for MULTILANGSTRING - empty multi lang string.

See Also

#### Reference

[MergedArticleReferencePropertyList Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList.html)
  
[MergedArticleReferencePropertyList Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList_members.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLE_ERPNR)