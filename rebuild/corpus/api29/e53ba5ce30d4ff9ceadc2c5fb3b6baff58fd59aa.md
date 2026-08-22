# GetProjectDataCompatibility Method

GetProjectDataCompatibility Method

Compares database schemas from current and given project. In the result of this check project could ok , need upgrade or just be incompatible.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public ProjectManager.DatabaseVersion.Status GetProjectDataCompatibility( 
   string projectPath
)
```
```

```
```
public:
ProjectManager.DatabaseVersion.Status GetProjectDataCompatibility( 
   String^ projectPath
)
```
```

#### Parameters

*projectPath*
:   Path to .elk project file.

#### Return Value

Returned value is status of project database.

Exceptions

| Exception | Description |
| --- | --- |
| [ProjectNotFoundException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectNotFoundException.html) | Thrown when project doesn't exist. |
| [System.ArgumentNullException](#) | Thrown when  `projectPath`  is `null`. |

See Also

#### Reference

[ProjectManager Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager.html)
  
[ProjectManager Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager_members.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~GetProjectDataCompatibility)