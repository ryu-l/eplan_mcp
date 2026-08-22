# Ged.Redraw

Ged.Redraw

Force a Redraw for the GED

Example

```
m_EventHandler = new EventHandler("Ged.Redraw");
m_EventHandler.EplanEvent += delegate {
    new Decider().Decide(EnumDecisionType.eOkDecision, "Ged.Redraw was called!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
};
```

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: Ged.Redraw)