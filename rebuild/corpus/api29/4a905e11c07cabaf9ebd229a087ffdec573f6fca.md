# CompleteInstallationSpaces Method

CompleteInstallationSpaces Method

Completes modification of installationspaces in the current revision of a project

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public void CompleteInstallationSpaces( 
   InstallationSpace[] spacesToComplete,
   string strIndex,
   string strRevDescription,
   string strReasonOfChange
)
```
```

```
```
public:
void CompleteInstallationSpaces( 
   array<InstallationSpace^>^ spacesToComplete,
   String^ strIndex,
   String^ strRevDescription,
   String^ strReasonOfChange
)
```
```

#### Parameters

*spacesToComplete*
:   An array of installation spaces to complete.

*strIndex*
:   New revision's name.

*strRevDescription*
:   New revision's description.

*strReasonOfChange*
:   Additional revision's description.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | \Internal interface necessary for the revision management could not be created. |
| **BaseException** | An error occurred, during the action. |

Remarks

When a logging revision starts, every changed installation space gets the marker "Draft" on it. With this function an installation space is completed, a revision is created (visible in the revision properties) and the draft is removed. When the revision belongs to an active project section, only the installationspaces of this section are completed.

See Also

#### Reference

[Revision Class](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision.html)
  
[Revision Members](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision_members.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~CompleteInstallationSpaces)