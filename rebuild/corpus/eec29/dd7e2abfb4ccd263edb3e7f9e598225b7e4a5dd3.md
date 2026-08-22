# Call of a Job (without callback)

The Job can be triggered by calling a URL in the browser ([HTTP](glossary_o_http.htm) GET) or via an HTTP Webservice call (HTTP POST). Any key-value pairs can be included in sending via the URL parameter (HTTP GET) or in the Request body (HTTP POST). These are accessed in the job definition via trigger.params.

![](../Pictures/Gui/ALL/note.png)Note:

HTTP GET and POST calls are not suitable for transferring larger data amounts to the Job Server. For larger data amounts it is advisable to only hand over references to the data that can then made be available in a sub system.

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example GET call:](javascript:void(0);)

```
http://aliasurl/jobs/request/myjob?mykey=1234&anotherkey=abcd
```

The progress page for the created Job is displayed as the response.

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example POST call:](javascript:void(0);)

|  |  |
| --- | --- |
| Request | POST /api/jobs/request/WebShopNoOutput HTTP/1.1 |
| Content-Type | application/json |
| Accept | application/json |
| Accept-Encoding | gzip, deflate |
| Pragma | no-cache |
| Body | ``` { 	"params": { 		"mykey":"1234", 		"anotherkey":"abcd" 	} } ``` |

![](../Pictures/Gui/ALL/note.png)Note:

All URL parameters specified are ignored in case of a POST call.

The Job object with status information at the moment of generation is given as the response. Further progress information has to be polled. Alternatively, calling of an external Webservice by the Job Server when the Job has been completed under specification of a callback URL is possible. For more information see [Call back by the Job Server](refjobserver_r_webservicetrigger_callback.htm).

![](../Pictures/Gui/ALL/example.png)[![Closed](../../Skins/Default/Stylesheets/Images/transparent.gif)Example POST Body with Callback URL:](javascript:void(0);)

|  |  |
| --- | --- |
| Body | ``` { 	"callback": { 		"href": "http://callbackurl" 	}, 	"params": { 		"mykey":"1234", 		"anotherkey":"abcd" 	} } ``` |