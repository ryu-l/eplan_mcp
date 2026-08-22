# RemovalOfUnnecessaryProjectStructuresIsEnabled Property

RemovalOfUnnecessaryProjectStructuresIsEnabled Property

Determines if removal of unnecessary project structures in the visible device tag should be forced. This property is need to be set, if you have a function with a visible name that contains project structures, you want to evaluate a new visible name and the project structures should be removed from the visible name if they matches the project structures of a surrounding location box or the page. By default or if this parameter is set to false, the project structures are kept in the visible name even if they are not necessary.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public bool RemovalOfUnnecessaryProjectStructuresIsEnabled {get; set;}
```
```

```
```
public:
property bool RemovalOfUnnecessaryProjectStructuresIsEnabled {
   bool get();
   void set (    bool value);
}
```
```

See Also

#### Reference

[NameService Class](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService.html)
  
[NameService Members](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService_members.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.NameService~RemovalOfUnnecessaryProjectStructuresIsEnabled)