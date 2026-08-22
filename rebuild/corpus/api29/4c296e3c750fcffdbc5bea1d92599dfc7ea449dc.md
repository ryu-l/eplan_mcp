# TargetIndex Property

TargetIndex Property

Terminal designation 1-base index.

Syntax

- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```
```
public int TargetIndex {get; set;}
```
```

```
```
public:
property int TargetIndex {
   int get();
   void set (    int value);
}
```
```

Remarks

This is a special feature for terminals, because the terminals have only a terminal number and the connection point designations are often empty. In such case routing algorithms can't decide which connection point will be used for a connection. The routing algorithms use the target index (first destination, second destination, ...) of a connection point in 2D, to determine the right terminal position in 3D or topologies.

See Also

#### Reference

[ConnectionPointPosition Class](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointPosition.html)
  
[ConnectionPointPosition Members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointPosition_members.html)

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointPosition~TargetIndex)