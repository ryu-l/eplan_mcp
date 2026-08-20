# XCMRemoveUnnecessaryNDPsAction

XCMRemoveUnnecessaryNDPsAction

```
 Removes unnecessary net definition points of active project.
```

  

| Parameter | Description |
| --- | --- |
| ``` Quiet ``` | ``` Suppresses message dialog if true. ``` |

**Remarks**

```
 Removes unnecessary net definition points of active project, i.e. net definition points that contain connections
 equal to the connections that would be in the net without using net based wiring but using target based wiring.
 If necessary, connection definition points are placed on the connections of the net so that connection properties don't get lost.
```

**Example**

```
 XCMRemoveUnnecessaryNDPsAction /Quiet:true
```

---

Eplan API, 18.03.2026, Â© by EPLAN GmbH & Co. KG. All rights reserved.

[Use the Eplan Global Support Portal for feedback and support](https://www.eplan.de/services/eplan-global-support/)