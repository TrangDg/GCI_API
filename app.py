import os, sys
src_folder = os.path.abspath('../GCI_API/src')
sys.path.insert(0, src_folder)
import json_mapping as j

from flask import Flask, request, send_from_directory, render_template, \
				  redirect, url_for

import json, csv
from cromulent.model import factory

app = Flask(__name__)

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# 404 error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Return html page 
@app.route('/gci/<ID>.html')
def sample_html(ID):
	# Return the json data of requested ID
	js = j.main(ID)
	try:
		sample_name = js["label"]
		return render_template('sample_info.html', ID=ID, name=sample_name)
	# Return 404 page if ID not in the database,
	# instead of raising 500 internal server error
	except:
		return render_template('404.html')

# Return json
@app.route('/gci/<ID>.json')
def sample_json(ID):	
	# Return the json data of requested ID
	js = j.main(ID)
	# If ID is not in the database, js is returned to None.
	# If None, return the 404 page instead of 'Null'
	if js is not None:
		return factory._buildString(js, compact=False)
	else:
		return render_template('404.html')

# Checking request content-type, if either 'html' or 'json',
# redirect to the appropriate route accordingly, 
# otherwise, return 'format_suggest.html' warning either 
# a typo occur or requested format is not supported.
@app.route('/gci/<ID>')
def sample(ID):
	if request.content_type == 'application/json':
		return redirect(url_for('sample_json', ID=ID))
	elif request.content_type == 'text/html':
		return redirect(url_for('sample_html', ID=ID))
	else:
		return render_template('format_suggest.html', ID=ID)
		

	




