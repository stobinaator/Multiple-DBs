#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:58:36 2021

@author: stobko
"""

from multi import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

class Lakers(db.Model):
    __bind_key__ = 'lal'
    __tablename__ = 'lakers players'
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String(50), nullable=False)
    team = db.Column(db.String(50), nullable=False)
    
    def json(self):
        return {'id': self.id, 'first name': self.first_name, 
                'last name': self.last_name, 'number': self.number,
                'age': self.age, 'position' : self.position,
                'team' : self.team, 'table' : self.get_tablename()}
    
    def add_player(_first_name, _last_name, _number, _age, _position, _team='LAL'):
        new_player = Lakers(first_name=_first_name, last_name=_last_name,
                               number=_number, age=_age, position=_position,
                               team = _team)
        db.session.add(new_player)
        db.session.commit()
        
    def get_all_players():
        return [Lakers.json(player) for player in Lakers.query.all()]
    
    def get_one_player(_id):
        return [Lakers.json(Lakers.query.filter_by(id=_id).first())]
    
    def update_player(_id, _first_name, _last_name, _number, _age, _position, _team='LAL'):
        player_to_update = Lakers.query.filter_by(id=_id).first()
        player_to_update.first_name = _first_name
        player_to_update.last_name = _last_name
        player_to_update.number = _number
        player_to_update.age = _age
        player_to_update.position = _position
        player_to_update.team = _team
        db.session.commit()
        
    def remove_player(_id):
        Lakers.query.filter_by(id=_id).delete()
        db.session.commit()
        
    def get_tablename(self):
        return self.__tablename__
    
    def get_player_id(self):
        return self.id