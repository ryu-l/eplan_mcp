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

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)