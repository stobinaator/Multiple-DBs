#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:06:36 2021

@author: stobko
"""

from flask import Flask 
import pathlib

path = pathlib.Path(__file__).parent.absolute()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{path}/mavericks.db'
app.config['SQLALCHEMY_BINDS'] = {'lal' : f'sqlite:///{path}/lakers.db',
                                  'bk' : f'sqlite:///{path}/brooklyn.db'}

