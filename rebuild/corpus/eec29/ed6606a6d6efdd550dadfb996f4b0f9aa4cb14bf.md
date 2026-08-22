# EPLAN Electric P8 configuration

The configuration file <EEC Installation Folder>\workspace\.metadata\.plugins\org.eclipse.core.runtime\.settings\com.mind8.ecad.eplanp8.prefs is additionally responsible for the configuration of EPLAN Electric P8.

In order to ensure that EPLAN Electric P8 does not hang up unnoticed you can set in the configuration file the number of calls for creating P8 data after which EPLAN Electric P8 is terminated.

Insert a line with the following syntax:

```
com.mind8.ecad.eplanp8.countdown=<count>
```

The value for <count> specifies the number of calls after which a restart of EPLAN Electric P8 is carried out.

EPLAN Electric P8 is restarted by the next call to create P8 data.