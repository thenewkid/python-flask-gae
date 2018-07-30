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
from google.appengine.ext.ndb import GenericProperty


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
    return str(BrightLandListing.search())


@app.route("/upload_json", methods=["post"])
def upload_json():
    try:
        d = request.get_json(force=True)
        BrightLandListing.store_listings(d)
        logging.info("\n\n")
        return "success"
    except Exception as e:
        logging.info(str(e))
        return "failure"


class BrightLandListing(ndb.Expando):
    ListOfficeKey = ndb.StringProperty()
    LotSizeUnits = ndb.StringProperty()
    ListAgentPreferredPhone = ndb.StringProperty()
    SchoolDistrictKey = ndb.StringProperty()
    MLSListDate = ndb.DateTimeProperty()
    Directions = ndb.StringProperty()
    Longitude = ndb.StringProperty()
    PricePerSquareFoot = ndb.StringProperty()
    SyndicationRemarks = ndb.StringProperty()
    LostSizeAcres = ndb.StringProperty()
    StreetName = ndb.StringProperty()
    ListAgentMlsId = ndb.StringProperty()
    Latitude = ndb.StringProperty()
    AssessmentYear = ndb.StringProperty()
    LotSizeArea = ndb.StringProperty()
    PublicRemarks = ndb.StringProperty()
    FullStreetAddress = ndb.StringProperty()
    TaxYear = ndb.StringProperty()
    ListingTaxID = ndb.StringProperty()
    ListAgentFullName = ndb.StringProperty()
    ListAgentEmail = ndb.StringProperty()
    ListAgentKey = ndb.StringProperty()
    LotSizeSquareFeet = ndb.StringProperty()
    PostalCode = ndb.StringProperty()
    UnparsedAddress = ndb.StringProperty()
    ListingKey = ndb.StringProperty()
    TaxAnnualAmount = ndb.StringProperty()
    CloseDate = ndb.DateTimeProperty()
    ListPrice = ndb.StringProperty()
    SubdivisionName = ndb.StringProperty()
    MlsStatus = ndb.StringProperty()
    ListingId = ndb.StringProperty()

    @classmethod
    def store_listings(cls, obj):
        new_listing = BrightLandListing()
        exists = cls.query(cls.ListingId == obj["ListingId"]).get()
        if not exists:
            for key in obj.keys():
                if key == "CloseDate" or key == "MLSListDate":
                    if obj[key]:
                        dt = parser.parse(obj[key])
                        setattr(new_listing, key, dt)
                    else:
                        setattr(new_listing, key, None)
                else:
                    setattr(new_listing, key, obj[key])
                    
            new_listing.put()
            logging.info("new listing stored")
        else:
            logging.info("listing id already exists")

    @classmethod
    def search(cls):
        total_set = []
        after_2016 = cls.query(cls.AssessmentYear > '2016').fetch(10)

        try:
            for obj in after_2016:
                jsonifyable = obj.to_dict()
                logging.info(type(jsonifyable["CloseDate"]))
                logging.info("\n")
                # total_set.append(json.dumps(jsonifyable))

        except Exception as e:
            logging.info(str(e))
            return total_set

        return json.dumps(total_set)












