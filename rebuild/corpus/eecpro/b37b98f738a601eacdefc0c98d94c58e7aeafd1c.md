# Set parameter values

All parameter values are strings in Java view, viz. setValue expects a string

To set formulas as parameter values, use the setPrettyValue() method instead of setValue(). Thus absolute type names become rugged against renaming the referenced classes.

### [ClosedExample code for setValue()](javascript:void(0);)

#### Requirements:

- The model data of install\scripting\scripting.eox have been imported.

The following script example (ScriptingExamples.setParameterValue1) determines the value of the parameter Option\_Inspect\_available of the project component Feeder.

If the value of the parameter true, it is set to the value false and vice versa.

For the example the SelectionAction setParameterValue1 has to be executed on any project component.

The name of the project component is specified (see row 12).

The name of the parameter is also specified (see row 15).

The determination of the mechatronic object is carried out with the method AbsoluteNameUtil.getObjectByAbsolutePath() (see row 22).

The getParameter() and getCalculatedValue() methods determine the specified parameter and its value (see row 27).

The setValue() method sets the value of the parameter either to true or to false (see rows 33 and 38).

The uow.saveChanges() method is used to make the change effective in the Unit-Of-Work in the project (see row 44).

Information is output in the message log (see rows 6, 14, 19, 24, 29, 35, 40 and 47).

```
import org.foederal.util.ui.messages.UserMessageCollector;
import com.mind8.mechatronic.skill.AbsoluteNameUtil;

String scriptName = "setParameterValue1";
String info = "### Start of script '" + scriptName + "' ###";
UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);

// determine the UnitOfWork
uow = self.getUnitOfWork();

// Absolute name of component containing the parameter
String absName = "Feeder_Extended1.Mechatronic.Feeder";
info = "absName: " + absName);
UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);

// Name of parameter
String parameterName = "Option_Inspect_available";
info = "parameterName: " + parameterName);
UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);

// Determine the mechatronic component
objectName = AbsoluteNameUtil.getObjectByAbsolutePath(absName,uow);
info = "objectName: " + objectName);
UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);

// Determine the current parameter value
parameterValue = objectName.getParameter(parameterName).getCalculatedValue();
info = "parameterValue: " + parameterValue);
UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);

// Toggle the parameter value of parameter "Option_Inspect_available" to "false" if "true" and vice versa
if(parameterValue == true){
	objectName.getParameter(parameterName).setValue("false");
	info = "Parameter set to 'false'");
	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
}
else{
	objectName.getParameter(parameterName).setValue("true");
	info = "Parameter set to 'true'");
	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
}

// save the change
uow.saveChanges();

info = "### End of script '" + scriptName + "' ###";
UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
```

### [ClosedSample code for setPrettyValue()](javascript:void(0);)

#### Requirements:

- The model data of install\scripting\scripting.eox have been imported.

The following script example (ScriptingExamples.setParameterValue2) determines the value of the FunctionDesignation parameter of the project component Feeder.

The formula =this.name is set as the value of the parameter.

For the example the SelectionAction setParameterValue1 has to be executed on each project component.

The name of the project component is specified (see row 14).

The name of the parameter is also specified (see row 17).

The determination of the mechatronic object is carried out with the method AbsoluteNameUtil.getObjectByAbsolutePath() (see row 22).

The setPrettyValue() method sets the value of the parameter to the =this.name formula (see row 27).

The uow.saveChanges() method is used to make the change effective in the Unit-Of-Work in the project (see row 32).

Information is output in the message log (see rows 6, 14, 19, 24, 29 and 35).

```
import org.foederal.apache.log4j.SpaceLogger;
import com.mind8.mechatronic.skill.AbsoluteNameUtil;

SpaceLogger logger = SpaceLogger.getSpaceLogger("My Logger");

String scriptName = "setParameterValue2";

logger.info("### Start of script '" + scriptName + "' ###");

// determine the UnitOfWork
uow = self.getUnitOfWork();

// Absolute name of component containing the parameter
String absName = "Feeder_Extended1.Mechatronic.Feeder";

// Name of parameter
String parameterName = "FunctionDesignation";
logger.info("parameterName: " + parameterName);

// Determine the mechatronic component
objectName = AbsoluteNameUtil.getObjectByAbsolutePath(absName,uow);
logger.info("objectName: " + objectName);

// Set the parameter value to "=this.name"
objectName.getParameter(parameterName).setPrettyValue("=this.name");
logger.info("Parameter set to '=this.name'");

// save the change
uow.saveChanges();

logger.info("### End of script '" + scriptName + "' ###");
```