# Next Forms

For certain report types (e.g. device tag list, cable assignment diagram, terminal-strip overview, etc.) it is possible to specify a next form. In reports, the next form is output after the current form. The next form can be inserted into the same page as the current form or on a subsequent page, and you define this using the insertion point of next form.

### Insertion point of next form

An Insertion point of next form can be placed in a form in order to insert another report at this point. This allows the generation of report blocks composed of two different forms. Together, all pages generated for a single form name define a report block.

It is also possible to insert several insertion points of next forms into a form. The report sequence is determined by the graphics.

Report type and form of the next form are entered at the insertion point of the next form. In addition you have the possibility to determine filter and sorting criteria for the extent and the sorting of the report.

All generated pages adopt the report type / page type from the main form (e.g. from the cable assignment diagram). The next report is only referenced on the page (like a nested report). Any Insertion points of next form in the next form are ignored.

### Report Types

Depending on the form type of the opened main form, different report types are available for next forms. For most form types, the "Summarized parts list" and the "Parts list" are available. "Identical form type" in the table means that, e.g., for the "Cable diagram" report type a next form of report type "Cable diagram" is possible.

| Main form | Next form | | | |
| Form type | Summarized parts list | Parts list | Identical form type | Additional |
| Assembly/Module overview |  |  | x |  |
| Device tag list | x | x |  |  |
| Cable assignment diagram | x | x |  |  |
| Cable diagram | x | x | x |  |
| Cable overview | x | x |  |  |
| Terminal line-up diagram | x | x |  | Terminal overview |
| Terminal-strip overview | x | x |  |  |
| Terminal diagram | x | x | x | Terminal line-up diagram |
| PLC diagram | x | x | x |  |
| PLC card overview | x | x |  |  |
| Plug diagram | x | x | x |  |
| Plug overview | x | x |  |  |
| Connection list | x | x |  |  |
| Topology: Routing path list | x | x |  |  |
| Topology: Routed cables / connections | x | x |  |  |
| Pre-planning: Planning object overview | x | x |  |  |
| Pre-planning: Planning object plan |  |  | x |  |
| Pre-planning: Structure segment plan |  |  | x |  |

See also

[Form and Plot Frame Editor](formeditorgui_k_start.htm)

[Dialog Insertion point of next form](formeditorgui_d_folgeformulareinfuegepunkt.htm)