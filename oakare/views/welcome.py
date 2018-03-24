from functools import wraps
import flask
from flask import session, redirect, url_for, request
import arrow
import oakare
from oakare.model import get_db
import os
from oakare.views.globals import *

@oakare.app.route('/', methods=['GET', 'POST'])
#@login_required
def show_welcome():
	'''Show the welcome page.'''

	context = {}
	context['username'] = 'ashvarma'
	context['user_first_name'] = 'Ashirvad'
	context['logo_url'] = get_logo_path()
	return flask.render_template("welcome.html", **context)
