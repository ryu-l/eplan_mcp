# Execute(String,ActionCallingContext) Method

Execute(String,ActionCallingContext) Method

Execution of a command line expression

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public virtual bool Execute( 
   string strExpression,
   ActionCallingContext oContext
)
```
```

```
```
public:
virtual bool Execute( 
   String^ strExpression,
   ActionCallingContext^ oContext
)
```
```

#### Parameters

*strExpression*
:   Action plus arguments

*oContext*
:   The context assigned to the action. Additional data can be encapsulated by the user here.

#### Return Value

â¢ TRUE if the command line operation was completed successfully  
â¢ FALSE if one or more errors occured while executing the command line operation

See Also

#### Reference

[CommandLineInterpreter Class](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter.html)
  
[CommandLineInterpreter Members](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter_members.html)
  
[Overload List](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter~Execute.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)