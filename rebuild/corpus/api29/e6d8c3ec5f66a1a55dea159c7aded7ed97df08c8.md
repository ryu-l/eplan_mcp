# IEplActionBatchExtension Interface Members

IEplActionBatchExtension Interface Members

The following tables list the members exposed by [IEplActionBatchExtension](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionBatchExtension.html).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [InterfaceName](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IInterface~InterfaceName.html) | This name is used to register the type as an interface. (Inherited from [Eplan.EplApi.ApplicationFramework.IInterface](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IInterface.html)) |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [GetBatchActionDisplayName](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionBatchExtension~GetBatchActionDisplayName.html) | Get the display name of this action |
| Method | [GetBatchActionName](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionBatchExtension~GetBatchActionName.html) | Get the action this interface belongs to |
| Method | [GetListOfSettings](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionBatchExtension~GetListOfSettings.html) | Get all relevant Settings for this action to be able to execute this action on oder computer and other user settings. |
| Method | [GetPageFilterParameterNameInContext](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionBatchExtension~GetPageFilterParameterNameInContext.html) | Get the page filter parameter name of the Context. This one is replaced by the project on the server. p.e. PAGEFILTERNAME |
| Method | [GetParameters](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionBatchExtension~GetParameters.html) | Get all parameters needed for this action. Set the needed parameters in the context. Open a dialog to get the parameters from user. |
| Method | [GetPersistentParameters](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionBatchExtension~GetPersistentParameters.html) | Fill all parameter names in the list which should be saved. They are saved in the scheme for auto proc. |
| Method | [GetProjectParameterInContext](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionBatchExtension~GetProjectParameterInContext.html) | Get the project parameter name of the Context. This one is replaced by the project on the server. |
| Method | [GetProjectRequirement](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionBatchExtension~GetProjectRequirement.html) | Return the project handling for this action |
| Method | [GetSelectionParameter](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionBatchExtension~GetSelectionParameter.html) | Get all parameter different for a project selection or a page selection when |

[Top](#top)

See Also

#### Reference

[IEplActionBatchExtension Interface](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionBatchExtension.html)
  
[Eplan.EplApi.ApplicationFramework Namespace](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework_namespace.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplActionBatchExtension)