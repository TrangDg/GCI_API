import os, sys
src_folder = os.path.abspath('../GCI_API/src')
sys.path.insert(0, src_folder)
import json_mapping as j

from flask import Flask, request, send_from_directory, render_template, \
				  redirect, url_for

import json, csv
from cromulent.model import factory

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



@app.route('/gci/<ID>.html')
def sample_html(ID):
	js = j.main(ID)
	try:
		sample_name = js["label"]
		return render_template('sample_info.html', ID=ID, name=sample_name)
	except:
		return render_template('404.html')


@app.route('/gci/<ID>.json')
def sample_json(ID):	
	js = j.main(ID)
	if js is not None:
		return factory._buildString(js, compact=False)
	else:
		return render_template('404.html')

@app.route('/gci/<ID>')
def sample(ID):
	if request.content_type == 'application/json':
		return redirect(url_for('sample_json', ID=ID))
	elif request.content_type == 'text/html':
		return redirect(url_for('sample_html', ID=ID))
	else:
		return render_template('format_suggest.html', ID=ID)
		

	




