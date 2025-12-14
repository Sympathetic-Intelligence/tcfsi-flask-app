from flask import Flask, request, jsonify, make_response, render_template, redirect, url_for, session
from flask import Markup
import requests
import ipinfo
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

application = Flask(__name__, template_folder='templates')


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

@application.route('/aspects')
def aspects():
    return render_template('aspects.html')

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

@application.route('/articles')
def articles():
    return render_template('articles.html')

@application.route('/contributing')
def contributing():
    return render_template('contributing.html')

@application.route('/contributing/volunteering')
def volunteering():
    return render_template('volunteering.html')

@application.route('/contributing/donations')
def donations():
    return render_template('donations.html')

@application.route('/little_book')
def little_book():

    # print(ipinfo.__version__)

    try:
        ip_address = request.remote_addr
        print(ip_address)


        access_token = '2148859d0efe1c'
        handler = ipinfo.getHandler(access_token)
        # ip_address = "109.79.233.60"
        details = handler.getDetails(ip_address)
        print(details.country)
        print(details.city)
        print(details.loc)
        print(details.postal)
        print(details.region)
        print(details.timezone)
        print(details.country_name)

        country = details.country
    except Exception as e:
        print(e)
        country = 'hello'
        
    return render_template('little_book.html', country=country)


@application.route('/contact')
def contact():
    return render_template('contact.html')

@application.route('/sos')
def sos():
    return render_template('sos.html')

@application.route('/aspects/processification')
def processification():
    return render_template('aspects/processification.html')

@application.route('/aspects/perspective_deficit')
def perspective_deficit():
    return render_template('aspects/perspective_deficit.html')

@application.route('/aspects/revisable_inference')
def revisable_inference():
    return render_template('aspects/revisable_inference.html')

@application.route('/aspects/presence_and_reflections')
def presence_and_reflections():
    return render_template('aspects/presence_and_reflections.html')

@application.route('/aspects/reflective_spontaneity')
def reflective_spontaneity():
    return render_template('aspects/reflective_spontaneity.html')

@application.route('/aspects/countering')
def countering():
    return render_template('aspects/countering.html')

@application.route('/aspects/subliminal_exposition')
def subliminal_exposition():
    return render_template('aspects/subliminal_exposition.html')

@application.route('/aspects/agency')
def agency():
    return render_template('aspects/agency.html')






# run the application.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production application.
    application.debug = True
    application.run()