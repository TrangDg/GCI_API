Currently, GCI exports their sample reference data to an 
excel spreadsheet. Using cromulent, the data is then mapped 
to JSON-LD with one file per sample. This project aims to 
set up a server that host all the JSON-LD files, and an
API that returns the requested file(s). 

*Set up directory*
	```
	>/src
	   ...flask code
	/data
	   /gci
	   		/sample
	   			...json files
	```
*Mapping csv to JSON-LD*
	* Change base url -- with ID = sample's Barcode?
	  e.g. 'localhost:port/gci/sample/WOOD10001'
	* Map csv data into JSON-LD
	* Export JSON-LD of each sample to a file, preferably 
	  named as the unique main ID
	 * Where to store the files? `data/gci/sample/WOOD10001.json`


*Creating API*
	* Set up an application using Flask (factory)
	* API: each json file accessed by manually typing the ID 
	       in the address bar?
		* Adding variables (ID) to url '/url/<variable>'
		* function: return the .json when the ID is requested
		  (url_for) 
		  * <localhost:5000/gci/sample/WOOD10001>
		  * google "content negotiation"
		  * return it with the content type (mime type) for JSON
		* Error handling: invalid ID? redirect? (to where)
		   -- https://httpstatuses.com/404

Requirement #2:
	* When you go to /<ID>, it should check if you request with text/html or application/json
	* If it's text/html, you should return a HTML page with basic information about the object.
		* it should do this by redircecting to /<ID>.html
	* if you request with content type application/json, you should redirect to /id.json and return the JSON itself.
	* This will require creating two new routes in the flask app.
	* Look into Postman app to help with making requests with content types


Requirement #3:
* Flask should call the crom code to generate the json data without saving on the disk.


REquirement:
* No crash - DO more tests