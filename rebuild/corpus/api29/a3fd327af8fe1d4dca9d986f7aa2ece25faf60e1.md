# OptimizeDistributedTerminals(TerminalStrip[],OptimizeDistributedTerminalsConfig) Method

OptimizeDistributedTerminals(TerminalStrip[],OptimizeDistributedTerminalsConfig) Method

Optimize all distributed terminals of the selected terminal strips

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool OptimizeDistributedTerminals( 
   TerminalStrip[] arrTerminalStrips,
   TerminalsService.OptimizeDistributedTerminalsConfig settings
)
```
```

```
```
public:
bool OptimizeDistributedTerminals( 
   array<TerminalStrip^>^ arrTerminalStrips,
   TerminalsService.OptimizeDistributedTerminalsConfig^ settings
)
```
```

#### Parameters

*arrTerminalStrips*
:   Array of terminal strips to process.

*settings*
:   A set of options for optimization process. If NULL, options last used in GUI are read from user settings.

#### Return Value

TRUE if operation succeeded, FALSE otherwise.

See Also

#### Reference

[TerminalsService Class](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.TerminalsService.html)
  
[TerminalsService Members](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.TerminalsService_members.html)
  
[Overload List](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.TerminalsService~OptimizeDistributedTerminals.html)
  
[TerminalsService.OptimizeDistributedTerminalsConfig Class](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.TerminalsService+OptimizeDistributedTerminalsConfig.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.TerminalsService~OptimizeDistributedTerminals(TerminalStrip[],OptimizeDistributedTerminalsConfig))