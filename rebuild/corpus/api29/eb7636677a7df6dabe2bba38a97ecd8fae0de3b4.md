# Message Class Members

Message Class Members

The following tables list the members exposed by [Message](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Message.html).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [MessageState](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Message~MessageState.html) | The MessageState determines the actual adjusted check type |

[Top](#top)

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [DoHelp](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Message~DoHelp.html) | Called by EPLAN when the help text to the message should be shown. the function itself must take care to call the matching help system with the correct language. The easiest way is to call a simple dialog or message box. |
| Public Method | [GetMessageText](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Message~GetMessageText.html) | Called by EPLAN when the message text should be shown. |
| Public Method | [OnRegister](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Message~OnRegister.html) | Called by EPLAN when the new project message is added to the system. If a new project message was added to a registered add-in, the add-in must be registered over again. |

[Top](#top)

See Also

#### Reference

[Message Class](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Message.html)
  
[Eplan.EplApi.EServices Namespace](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices_namespace.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Message)