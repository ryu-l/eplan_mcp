# ArePlanningObjectsStructureMerged Property

ArePlanningObjectsStructureMerged Property

Indicates whether planning objects structure will be merged with existing nodes or renumbered and added.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool ArePlanningObjectsStructureMerged {get; set;}
```
```

```
```
public:
property bool ArePlanningObjectsStructureMerged {
   bool get();
   void set (    bool value);
}
```
```

Remarks

This flag is used in situation when structure of pre-planning objects imported from macro, contains nodes which already exists in project. If `ArePlanningObjectsStructureMerged` is `true` then all children of duplicated node are added to coresponding nore from project. If value is `false` then new name is assigned to such node and it is added to project with all its children.

See Also

#### Reference

[Insert Class](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert.html)
  
[Insert Members](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert_members.html)

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)