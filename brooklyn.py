#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:58:44 2021

@author: stobko
"""

from multi import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

class Brooklyn(db.Model):
    __bind_key__ = 'bk'
    __tablename__ = 'brooklyn players'
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String(2), nullable=False)
    team = db.Column(db.String(50), nullable=False)
    info = db.Column(db.String(200), nullable=False)
    
    def json(self):
        return {'id': self.id, 'first name': self.first_name, 
                'last name': self.last_name, 'number': self.number,
                'age': self.age, 'position' : self.position,
                'team' : self.team, 'table' : self.get_tablename(),
                'info': self.info}
    
    def add_player(request_data):
        new_player = Brooklyn(first_name=request_data['first_name'],
                               last_name=request_data['last_name'],
                               number=request_data['number'],
                               age=request_data['age'],
                               position=request_data['position'],
                               team='BKN', info = request_data['info'])
        
        db.session.add(new_player)
        db.session.commit()
    
        
    def get_all_players():
        return [Brooklyn.json(player) for player in Brooklyn.query.all()]
    
    def get_one_player(_id):
        return [Brooklyn.json(Brooklyn.query.filter_by(id=_id).first())]
    
    def update_player(_id, request_data, _team='BKN'):
         player_to_update = Brooklyn.query.filter_by(id=_id).first()
         player_to_update.first_name = request_data['first_name']
         player_to_update.last_name = request_data['last_name']
         player_to_update.number = request_data['number']
         player_to_update.age = request_data['age']
         player_to_update.position = request_data['position']
         player_to_update.team = _team
         player_to_update.info = request_data['info']
         db.session.commit()
        
    def remove_player(_id):
        Brooklyn.query.filter_by(id=_id).delete()
        db.session.commit()
        
    def get_tablename(self):
        return self.__tablename__
    
    def get_player_id(self):
        return self.id
    
    def get_player_info(self):
        return self.info
    
    def get_player_by_first_name(first):
        i = 0
        p_dict = {}
        p_list = Brooklyn.query.filter_by(first_name=first).all()
        for p in p_list:
            p_dict[i] = Brooklyn.json(p)
            i += 1
            
        if len(p_dict) == 0:
            return 0
        else:
            return p_dict
    
    def get_player_by_last_name(last):
        i = 0
        p_dict = {}
        p_list = Brooklyn.query.filter_by(last_name=last).all()
        for p in p_list:
            p_dict[i] = Brooklyn.json(p)
            i += 1
            
        if len(p_dict) == 0:
            return 0
        else:
            return p_dict
    
    def get_player_by_pos(pos):
        i = 0
        p_dict = {}
        p_list = Brooklyn.query.filter_by(position=pos).all()
        for p in p_list:
            p_dict[i] = Brooklyn.json(p)
            i += 1
            
        if len(p_dict) == 0:
            return 0
        else:
            return p_dict
    
    def get_player_by_accomp(accomp):
        i = 0
        p_dict = {}
        p_list = Brooklyn.get_all_players()
        final_list = []
        for p in p_list:
            p_dict[i] = p
            i+=1
        for p in p_dict:
            accomplishments = p_dict[p]['info']
            accomp_list = accomplishments.split(';')
            for a in accomp_list:   
                if accomp in a:
                    index = a.find(accomp)
                    number = a[index-3:index-1]
                    number = number.strip()
                    if number != '0':
                        final_list.append(p_dict[p]) 
        if len(final_list) == 0:
            return 0
        else:
            return final_list