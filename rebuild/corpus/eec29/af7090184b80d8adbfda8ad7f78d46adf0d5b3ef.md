# perform(String sqlStatement)

Returns a list of all resulting objects of the SQL query to the data source. Each object represents a row of the result. These objects can be accessed by methods that match the requested column names of the data source object. For calculated column names the method property(<column name>) is available.

Example:

The result of perform('select ArticleNumber, Vendor from [Article$] where Vendor=\'Mind8\';') can be accessed by the methods ArticleNumber and Vendor.

| **perform([String](glossary_o_string.htm) sqlStatement)** | | | | |
| --- | --- | --- | --- | --- |
| Argument | String | sqlStatement | SQL query to the data source | |
| Return value | List | |  | |

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example](javascript:void(0);)

| Formula | Result |
| --- | --- |
| ``` =type('Baukasten.Stückliste.ArtikelDB') .perform('select Artikelnummer,Artikeltyp,Hersteller from Artikel where Hersteller=\'Balluff\'  and record.Artikeltyp=\'Endschalter\';') ``` | ``` [[12,Endschalter,Balluff],  [15,583,Endschalter,Balluff]] ``` |