#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
from flask import Flask, redirect, render_template, request, jsonify, url_for
import jinja2
import os
import json
import logging
from dateutil import parser
import time

# flask app and jinja2 settings
from google.appengine.ext import ndb

def create_flask_app():
    app = Flask(__name__)
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)
    app.jinja_env = jinja_env
    app.debug = True
    return app

app = create_flask_app()


@app.route("/")
def index():
    return "Hola Ulisse"











