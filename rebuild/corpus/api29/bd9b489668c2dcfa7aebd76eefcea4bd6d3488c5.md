# XSDPreviewAction

XSDPreviewAction

```
 open or close the preview of a project page or macro
```

  

| Parameter | Description |
| --- | --- |
| PROJECTNAME | ``` name of the project; if the path is missing, the default value is used (see $(MD_PROJECTS)) ``` |
| PAGENAME | ``` name of page as string ``` |
| MACRONAME | ``` complete path to a window or page macro (with extension); if the path is missing, the default value is used (see $(MD_MACROS)) ``` |
| SHOW | ``` 1: the preview of the page/macro will be opened; 0: the preview will be closed ``` |

Remarks

```
 if PAGENAME and MACRONAME are empty, all pages of the project will be displayed in the preview
```

Example

```
 Preview of a page:
 
 XSDPreviewAction /PROJECTNAME:ESS_Sample_Project /PAGENAME:=CA1+EAA/1
 
 XSDPreviewAction /PROJECTNAME:"C:\\Users\\Public\\EPLAN\\Electric P8\\Projects\\EPLAN\\ESS_Sample_Project" /PAGENAME:=CA1+EAA/2
 
 Preview of a window macro:
 
 XSDPreviewAction /PROJECTNAME:ESS_Sample_Project /MACRONAME:Macro_0001.ema
 
 XSDPreviewAction /PROJECTNAME:$(MD_PROJECTS)\\ESS_Sample_Project /MACRONAME:$(MD_MACROS)\\Macro_0001.ema
```

---

EPLAN API , 21.05.2020, Â© by EPLAN Software and Service GmbH and Co. KG. All rights reserved.

[Send Feedback](mailto:Support-API@eplan.de?subject=Documentation Feedback: XSDPreviewAction )