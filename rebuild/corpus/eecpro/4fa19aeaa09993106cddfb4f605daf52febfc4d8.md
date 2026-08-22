# getPlaceholderObjects(Placeholder placeholder)

Returns a list of all objects, which are placed on the placeholder placeholder in this mechatronic component.

| getPlaceholderObjects(Placeholder placeholder) | | | |
| --- | --- | --- | --- |
| Argument | Placeholder | placeholder | A placeholder of the component. |
| Return value | List | | List of mechatronic objects |

### [ClosedExample code in Groovy](javascript:void(0);)

```
placeholder = component.getPlaceholders("T_Interfaces.ISchematicPage").get(0);
objects = component.getPlaceholderObjects(placeholder);
```

Result:

```
[<<M_WiringDiagram>>,<<M_SchematicPage>>,<<M_SchematicPage2>>]
```