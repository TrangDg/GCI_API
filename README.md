# GCI_API

Currently, GCI exports their sample reference data to an excel spreadsheet. Using cromulent, the data is then mapped to JSON-LD. This project aims to set up a server that host all the JSON-LD, and an API that returns the requested data, based on negotiated content type.

#### /src

This folder contains the code 'json_mapping.py' mapping the csv data to json-ld. The csv can be found 
in folder '../data'.

#### app.py

Flask code set up the server and running API. To run the code:
* Install with pipenv: flask, cromulent, dateparser. $ pip install <package>
  Pipenv automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages (*Sources*: [pipenv](https://pipenv.readthedocs.io/en/latest/#)). Instruction for installing pipenv can be found [here](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv). 
* Environment variables can be found in the *.env* file. This will be automatically loaded once flask is run through pipenv. 
* To run flask, use the command line: $ pipenv run flask run

*Notes*: Currently, user can request the data for each sample by manually entered the sample ID to the url, i.e. 'your_localhost:the_port/gci/<sample_ID>'. JSON data is not stored on disk. Instead, each time a sample_ID is called, the app will process the mapping. 
  * When user only enters the ID without extension (.html or .json), user will be redirected to the url '/gci/<ID>.html' or '/gci/<ID>.json', depending on the requested content-type. However, if the requested content-type is not supported, e.g. 'application/pdf', the app will display 'format_suggest.html', including the links to HTML and JSON formats. 
  * HTML page only displays the sample label for now.
  * JSON page displays the string format of the json data.

#### Testing with Cypress
The API is tested using cypress. Click [here](https://docs.cypress.io/guides/getting-started/installing-cypress.html) for installing instruction. 
The testing code 'sample_spec.js' can be found in /cypress/integration, including:
1. Loading homepage
2. When user enter *only* the sample ID, without extension, 'localhost:port/gci/<sample_ID>', given the ID is **correct** :
  * If content-type is 'text/html', user is redirected to url '/gci/<ID>.html'.
  * If content-type is 'application/json', user is redirected to url '/gci/<ID>.json'.
  * If content-type is neither of the above, 'format_suggest.html' should be loaded. Then:
   Testing the links to the sample's html and json 
3. Testing typo:
  * For now, the 'format_suggest.html' contains both the warning for the url typo as well as unsupported content type. However, if it's a typo, clicking on either HTML or JSON links should return the 404 error page. <Working on separating the 2 different errors>

*Notes*: the above tests also works when user enters url with extensions. 








