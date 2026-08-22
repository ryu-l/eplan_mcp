# ImportAssignmentList(Project,String,String,String,String,String,Boolean,Boolean) Method

ImportAssignmentList(Project,String,String,String,String,String,Boolean,Boolean) Method

Imports PLC assignment lists.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void ImportAssignmentList( 
   Project oProject,
   string strConfigurationProject,
   string strStation,
   string strCPU,
   string strLanguage,
   string strAssignmentListFileName,
   bool bCompByAddress,
   bool bAcceptInvAddr
)
```
```

```
```
public:
void ImportAssignmentList( 
   Project^ oProject,
   String^ strConfigurationProject,
   String^ strStation,
   String^ strCPU,
   String^ strLanguage,
   String^ strAssignmentListFileName,
   bool bCompByAddress,
   bool bAcceptInvAddr
)
```
```

#### Parameters

*oProject*
:   Project into which the PLC assignment list will be imported.

*strConfigurationProject*
:   PLC configuration project name

*strStation*
:   PLC station name

*strCPU*
:   PLC CPU.

*strLanguage*
:   Language shortcut for the import, e.g. "en\_US".

*strAssignmentListFileName*
:   Alternative file name and path. If empty parameter will be taken from plc schema.

*bCompByAddress*
:   If set to true, the PLC address is used as reference value.

*bAcceptInvAddr*
:   If set to true, even invalid addresses will be read.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing parameters. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the given Project does not exist or isn't valid. |
| **ApplicationException** | \Internal interface for importing PLC data could not be created. |
| **BaseException** | An error occurred during the import. |

Remarks

If no scheme name (strScheme) is passed, the last-used scheme will be used which is currently set in GUI. The name of the file to import is defined in the scheme.

See Also

#### Reference

[PlcService Class](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService.html)
  
[PlcService Members](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService_members.html)
  
[Overload List](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService~ImportAssignmentList.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService~ImportAssignmentList(Project,String,String,String,String,String,Boolean,Boolean))