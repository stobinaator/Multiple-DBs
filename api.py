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

""" DALLAS MAVERICKS """

@app.route('/roster/mavs', methods=['GET'])
def get_mavs_roster():
    return jsonify({'Mavs Roster' : Mavericks.get_all_players()})

@app.route('/roster/mavs/<int:id>', methods=['GET'])
def get_mavs_player_by_id(id):
    return_value = Mavericks.get_one_player(id)
    return jsonify(return_value)

@app.route('/roster/mavs', methods=['POST'])
def add_mavs_player():
    request_data = request.get_json()
    Mavericks.add_player(request_data['first_name'],
                                 request_data['last_name'], 
                                 request_data['number'],
                                 request_data['age'], 
                                 request_data['position'])
    response = Response("Mavs player added to roster", status=201, 
                                        mimetype='application/json')
    return response

@app.route('/roster/mavs/<int:id>', methods=['PUT'])
def update_mavs_player(id):
    request_data = request.get_json()
    Mavericks.update_player(id, request_data['first_name'],
                                    request_data['last_name'], 
                                    request_data['number'],
                                    request_data['age'],
                                    request_data['position'])
    response = Response("Mavs player updated", status=200, 
                                        mimetype='application/json')
    return response

@app.route('/roster/mavs/<int:id>', methods=['DELETE'])
def remove_mavs_player(id):
    Mavericks.remove_player(id)
    response = Response("Mavs player removed from roster", status=200,
                                        mimetype='application/json')
    return response


""" LOS ANGELES LAKERS """

@app.route('/roster/lakers', methods=['GET'])
def get_lakers_roster():
    return jsonify({'LA''s Roster' : Lakers.get_all_players()})

@app.route('/roster/lakers/<int:id>', methods=['GET'])
def get_lakers_player_by_id(id):
    return_value = Lakers.get_one_player(id)
    return jsonify(return_value)

@app.route('/roster/lakers', methods=['POST'])
def add_lakers_player():
    request_data = request.get_json()
    Lakers.add_player(request_data['first_name'],
                                 request_data['last_name'], 
                                 request_data['number'],
                                 request_data['age'], 
                                 request_data['position'])
    response = Response("LA's player added to roster", status=201, 
                                        mimetype='application/json')
    return response

@app.route('/roster/lakers/<int:id>', methods=['PUT'])
def update_lakers_player(id):
    request_data = request.get_json()
    Lakers.update_player(id, request_data['first_name'],
                                    request_data['last_name'], 
                                    request_data['number'],
                                    request_data['age'],
                                    request_data['position'])
    response = Response("LA's player updated", status=200, 
                                        mimetype='application/json')
    return response

@app.route('/roster/lakers/<int:id>', methods=['DELETE'])
def remove_lakers_player(id):
    Lakers.remove_player(id)
    response = Response("LA's player removed from roster", status=200,
                                        mimetype='application/json')
    return response

""" BROOKLYN NETS """

@app.route('/roster/brooklyn', methods=['GET'])
def get_brooklyn_roster():
    return jsonify({'Brooklyn''s Roster' : Brooklyn.get_all_players()})

@app.route('/roster/brooklyn/<int:id>', methods=['GET'])
def get_brooklyn_player_by_id(id):
    return_value = Brooklyn.get_one_player(id)
    return jsonify(return_value)

@app.route('/roster/brooklyn', methods=['POST'])
def add_brooklyn_player():
    request_data = request.get_json()
    Brooklyn.add_player(request_data['first_name'],
                                 request_data['last_name'], 
                                 request_data['number'],
                                 request_data['age'], 
                                 request_data['position'])
    response = Response("Brooklyn's player added to roster", status=201, 
                                        mimetype='application/json')
    return response

@app.route('/roster/brooklyn/<int:id>', methods=['PUT'])
def update_brooklyn_player(id):
    request_data = request.get_json()
    Brooklyn.update_player(id, request_data['first_name'],
                                    request_data['last_name'], 
                                    request_data['number'],
                                    request_data['age'],
                                    request_data['position'])
    response = Response("Brooklyn's player updated", status=200, 
                                        mimetype='application/json')
    return response

@app.route('/roster/brooklyn/<int:id>', methods=['DELETE'])
def remove_brooklyn_player(id):
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