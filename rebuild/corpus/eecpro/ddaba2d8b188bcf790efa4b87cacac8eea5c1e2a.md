# Inserting ECAD objects into a project

The ECAD structure can be built directly in a project by adding (instantiating) ECAD objects to a project directly from libraries (using Drag & Drop or via the popup menu).

This direct instantiation of ECAD objects, which is explained in the following subsections, is useful for tests and / or the understanding of the context in EEC during the initial training period.

The indirect route via mechatronic components is recommended: In the library, ECAD objects are assigned to mechatronic components (see [Link between mechatronic and discipline-specific components](eecbase_k_linking_dcs.htm)), a macro that represents a limit switch, for example, of the mechatronic component Limit switch. Only mechatronic components can be integrated into a project (see [Inserting mechatronic components in a project](eecbase_k_insert_mcs.htm)). The ECAD structure is then derived automatically from the mechatronic configuration (see [Generate structure](eecbase_k_linking_dcs_generate_structure.htm)).