#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:00:34 2021

@author: stobko
start with python3 api.py
"""
from mavericks import Mavericks
from lakers import Lakers
from brooklyn import Brooklyn
from multi import app
from flask import request, Response, jsonify


@app.route('/roster/<string:name>', methods=['GET'])
def get_roster(name):
    if name == 'Mavericks':
        return jsonify({'Roster' : Mavericks.get_all_players()})
    if name == 'Lakers':
        return jsonify({'Roster' : Lakers.get_all_players()})
    if name == 'Brooklyn':
        return jsonify({'Roster' : Brooklyn.get_all_players()})


@app.route('/roster/<string:name>/<int:id>', methods=['GET'])
def get_player_by_id(name,id):
    if name == 'Mavericks':
        return_value = Mavericks.get_one_player(id)
        return jsonify(return_value)
    if name == 'Lakers':
        return_value = Lakers.get_one_player(id)
        return jsonify(return_value)
    if name == 'Brooklyn':
        return_value = Brooklyn.get_one_player(id)
        return jsonify(return_value)


@app.route('/roster/<string:name>', methods=['POST'])
def add_player(name):
    if name == 'Mavericks':
        request_data = request.get_json()
        Mavericks.add_player(request_data['first_name'],
                             request_data['last_name'], 
                             request_data['number'],
                             request_data['age'], 
                             request_data['position'])
        response = Response("Mavs player added to roster", status=201, 
                                                mimetype='application/json')
        return response
    if name == 'Lakers':
        request_data = request.get_json()
        Lakers.add_player(request_data['first_name'],
                          request_data['last_name'], 
                          request_data['number'],
                          request_data['age'], 
                          request_data['position'])
        response = Response("LA's player added to roster", status=201, 
                                        mimetype='application/json')
        return response
    if name == 'Brooklyn':
        request_data = request.get_json()
        Brooklyn.add_player(request_data['first_name'],
                                 request_data['last_name'], 
                                 request_data['number'],
                                 request_data['age'], 
                                 request_data['position'])
        response = Response("Brooklyn's player added to roster", status=201, 
                                        mimetype='application/json')
        return response
    
    
@app.route('/roster/<string:name>/<int:id>', methods=['PUT'])
def update_player(name, id):
    if name == 'Mavericks':
        request_data = request.get_json()
        Mavericks.update_player(id, request_data['first_name'],
                                        request_data['last_name'], 
                                        request_data['number'],
                                        request_data['age'],
                                        request_data['position'])
        response = Response("Mavs player updated", status=200, 
                                            mimetype='application/json')
        return response
    if name == 'Lakers':
        request_data = request.get_json()
        Lakers.update_player(id, request_data['first_name'],
                                    request_data['last_name'], 
                                    request_data['number'],
                                    request_data['age'],
                                    request_data['position'])
        response = Response("LA's player updated", status=200, 
                                        mimetype='application/json')
        return response
    if name == 'Brooklyn':
        request_data = request.get_json()
        Brooklyn.update_player(id, request_data['first_name'],
                                    request_data['last_name'], 
                                    request_data['number'],
                                    request_data['age'],
                                    request_data['position'])
        response = Response("Brooklyn's player updated", status=200, 
                                        mimetype='application/json')
        return response
    

@app.route('/roster/<string:name>/<int:id>', methods=['DELETE'])
def remove_mavs_player(name, id):
    if name == 'Mavericks':
        Mavericks.remove_player(id)
        response = Response("Mavs player removed from roster", status=200,
                                            mimetype='application/json')
        return response
    if name == 'Lakers':
        Lakers.remove_player(id)
        response = Response("LA's player removed from roster", status=200,
                                            mimetype='application/json')
        return response
    if name == 'Brooklyn':
        Brooklyn.remove_player(id)
        response = Response("Brooklyn's player removed from roster", status=200,
                                            mimetype='application/json')
        return response
    


@app.route('/all/search/<string:last_name>', methods=['GET'])
def get_player_by_name(last_name):
    
    players_list = []
    if Mavericks.query.filter_by(last_name=last_name).first() != None:
        players_list.append(Mavericks.json(Mavericks.query.filter_by(last_name=last_name).first()))
    
    if Lakers.query.filter_by(last_name=last_name).first() != None:
        players_list.append(Lakers.json(Lakers.query.filter_by(last_name=last_name).first()))
    
    if Brooklyn.query.filter_by(last_name=last_name).first() != None:
        players_list.append(Brooklyn.json(Brooklyn.query.filter_by(last_name=last_name).first()))
    
    if not players_list:
        response = Response("There is no player with that name", status=200,
                                     mimetype='application/json')
        return response
    else:
        
        response = Response(str(players_list), status=200, mimetype='application/json')
        return response


if __name__ == '__main__':
    app.run(port=1234, debug=True)