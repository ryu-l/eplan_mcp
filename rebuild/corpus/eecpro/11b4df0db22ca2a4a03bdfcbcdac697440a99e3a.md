# systemProperty(String propertyName)

System methods

Determines the value of the given system property or null, if the value is not set.

| **systemProperty(String propertyName)** | | | | |
| --- | --- | --- | --- | --- |
| Argument | String | propertyName | System property whose value is queried | |
| Return value | String | | Value of the system property | |

### [ClosedExamples](javascript:void(0);)

| Formula | Result |
| --- | --- |
| =type('Engineering.System').systemProperty('user.home') | C:\Users\MyUsername |