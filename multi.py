#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:06:36 2021

@author: stobko
"""

from flask import Flask 


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/stobko/dev/bachelor/multiple_dbs/mavericks.db'
app.config['SQLALCHEMY_BINDS'] = {'lal' : 'sqlite:////Users/stobko/dev/bachelor/multiple_dbs/lakers.db',
                                  'bk' : 'sqlite:////Users/stobko/dev/bachelor/multiple_dbs/brooklyn.db'}

