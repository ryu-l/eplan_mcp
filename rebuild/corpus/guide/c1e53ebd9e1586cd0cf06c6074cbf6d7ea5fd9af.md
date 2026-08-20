# P502002: The image file '<x>' entered at the part does not exist

### Cause

In the parts database to be checked a part was found where an image file was entered which Eplan cannot find.

### Solution

1. In the parts management mark the line with the message in the Messages tab and select the Go to popup menu item for this line.  
   ![](../Pictures/Gui/ALL/arrow.png) The respective part is marked in the tree view of the parts management.
2. Bring the Properties tab to the front.
3. In the property table click [...] in the hierarchy level Mounting data in the value field of the Image file property and in the selection dialog opening select an existing image file from one of the offered image directories.  
     
   Or alternatively to this, delete the entered image file in the value field of the property.  
     
   Or create a new image, store it in the desired image directory and select it again at the property.
4. Click [Apply].
5. If required, start a new check run.
6. Close the parts management and perform a parts data synchronization.