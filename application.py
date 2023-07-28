from flask import Flask, request, jsonify, make_response, render_template, redirect, url_for, session
from flask import Markup
from collections import defaultdict
import operator
import numpy as np
import json
import time 
import math

import os
from tqdm import tqdm
import ast
import re
import uuid, hashlib, datetime, math, urllib

application = Flask(__name__)


@application.route('/')
def home():
    return render_template('index.html')

@application.route('/concept_home')
def concept_home():
    return render_template('concept_home.html')

@application.route('/center_home')
def center_home():
    return render_template('center_home.html')

@application.route('/tiers')
def tiers():
    return render_template('tiers.html')

@application.route('/origins')
def origins():
    return render_template('origins.html')

@application.route('/depthfulness')
def depthfulness():
    return render_template('depthfulness.html')

@application.route('/socioneurology')
def socioneurology():
    return render_template('socioneurology.html')

@application.route('/applications')
def applications():
    return render_template('applications.html')

@application.route('/research')
def research():
    return render_template('research.html')

@application.route('/videos')
def videos():
    return render_template('videos.html')

@application.route('/components')
def components():
    return render_template('components.html')

@application.route('/about')
def about():
    return render_template('about.html')

@application.route('/about/mission')
def mission():
    return render_template('mission.html')

@application.route('/about/board')
def board():
    return render_template('board.html')

@application.route('/panels')
def panels():
    return render_template('panels.html')

@application.route('/panels/police')
def police_panel():
    return render_template('police_panel.html')

@application.route('/panels/arts')
def arts_panel():
    return render_template('arts_panel.html')

@application.route('/panels/education')
def education_panel():
    return render_template('education_panel.html')

@application.route('/panels/healthcare')
def healthcare_panel():
    return render_template('healthcare_panel.html')

@application.route('/publications')
def publications():
    return render_template('publications.html')

@application.route('/contributing')
def contributing():
    return render_template('contributing.html')

@application.route('/contributing/volunteering')
def volunteering():
    return render_template('volunteering.html')

@application.route('/contributing/donations')
def donations():
    return render_template('donations.html')


@application.route('/contact')
def contact():
    return render_template('contact.html')

@application.route('/sos')
def sos():
    return render_template('sos.html')


# run the application.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production application.
    application.debug = True
    application.run()