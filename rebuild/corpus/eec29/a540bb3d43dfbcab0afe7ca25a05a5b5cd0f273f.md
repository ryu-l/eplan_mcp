# Support for variants of window macros

Window macros with all representation types and variants are supported. The variants of window macros are identified by the representation type (Neutral, Single-Line, Multi-Line, Graphic, etc.) and the variant (A, B, C, etc.). Corresponding model variables exist for these parameters. When importing a window macro, the parameters Representation type and Variant are generated, provided they exist in the window macro.

The use of window macros has the advantage that only one discipline component with one resource has to be created. In the parameter view of the discipline component, the parameters Representation type and Variant (if available) must be added, and, for example, filled with a permissible value via a formula.

![](../Pictures/Gui/ALL/note.png)Note:

The same parameters should be created in all variants of a window macro, because formulas that reference missing parameters of a variant would otherwise cause aborting during generation of the schematic.

![](../Pictures/Gui/ALL/note.png)Note:

During the synchronization of the external resource, EEC collects all the parameters from all variants. It is not an error if a parameter of the same type appears in different variants. If it is missing from a variant, it is not an error either.

If during the generation process EEC finds a window macro with several variants, it will use the model variables Name Of The Parameter For The Representation Type of Window Macros and Name Of The Parameter For The Variant of Window Macros in order to select the correct variant. If these model variables are not specified, the generation process is terminated, and a corresponding error message is shown.

See also:

[Parameter Name For The Window Macro Variant](admin_r_modelvar_p8variant.htm)

[Parameter name for the window macro representation type](admin_r_modelvar_p8representationtype.htm)