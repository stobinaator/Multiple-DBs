#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:00:34 2021

@author: stobko
"""

from mavericks import Mavericks
from lakers import Lakers
from brooklyn import Brooklyn
from multi import app
from flask import request, Response, jsonify

URLS_LIST = ['/rosters' ,'/roster/<string:name>', '/roster/<string:name>/<int:id>',
              '/all/search/last/<string:last_name>','/all/search/first/<string:first_name>',
              '/all/search/position/<string:pos>','/all/search/accomplishments/<string:information>']


@app.route('/rosters', methods=['GET'])
def get_rosters():
    return jsonify({'Rosters' : [{'Mavericks' : Mavericks.get_all_players()},
                                 {'Lakers' : Lakers.get_all_players()},
                                 {'Brooklyn' :Brooklyn.get_all_players()}]})


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
    try:
        if name == 'Mavericks':
            return jsonify(Mavericks.get_one_player(id))
        if name == 'Lakers':
            return jsonify(Lakers.get_one_player(id))
        if name == 'Brooklyn':
            return jsonify(Brooklyn.get_one_player(id))
    except Exception:
         response = Response("There is no player with this ID", status=200,
                                            mimetype='application/json')
         return response

@app.route('/roster/<string:name>', methods=['POST'])
def add_player(name):
    if name == 'Mavericks':
        request_data = request.get_json()
        Mavericks.add_player(request_data)
        response = Response("Mavs player added to roster", status=201, 
                                                mimetype='application/json')
        return response
    
    if name == 'Lakers':
        request_data = request.get_json()
        Lakers.add_player(request_data)
        response = Response("LA's player added to roster", status=201, 
                                        mimetype='application/json')
        return response
    
    if name == 'Brooklyn':
        request_data = request.get_json()
        Brooklyn.add_player(request_data)
        response = Response("Brooklyn's player added to roster", status=201, 
                                        mimetype='application/json')
        return response
    
    
@app.route('/roster/<string:name>/<int:id>', methods=['PUT'])
def update_player(name, id):
    try:
        if name == 'Mavericks':
            request_data = request.get_json()
            Mavericks.update_player(id, request_data)
            response = Response("Mavs player updated", status=200, 
                                                mimetype='application/json')
            return response
        
        if name == 'Lakers':
            request_data = request.get_json()
            Lakers.update_player(id, request_data)
            response = Response("LA's player updated", status=200, 
                                            mimetype='application/json')
            return response
        
        if name == 'Brooklyn':
            request_data = request.get_json()
            Brooklyn.update_player(id,request_data)
            response = Response("Brooklyn's player updated", status=200, 
                                            mimetype='application/json')
            return response
    except Exception:
        response = Response("There is no player with this ID", status=200,
                                            mimetype='application/json')
        return response
         

@app.route('/roster/<string:name>/<int:id>', methods=['DELETE'])
def remove_player(name, id):
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
          
 
@app.route('/all/search/last/<string:last_name>', methods=['GET'])
def get_player_by_lastname(last_name):
    
    players_list = []
    mavs_dict = Mavericks.get_player_by_last_name(last_name)
    la_dict = Lakers.get_player_by_last_name(last_name)
    bk_dict= Brooklyn.get_player_by_last_name(last_name)
    
    players_list = check_length(mavs_dict, la_dict, bk_dict)
    
    if not players_list:
        response = Response("There is no player with that last name.", status=200,
                                     mimetype='application/json')
        return response
    else:
        return jsonify({'Last Name' : players_list})
   
@app.route('/all/search/first/<string:first_name>', methods=['GET'])
def get_player_by_firstname(first_name):
    
    players_list = []
    mavs_dict = Mavericks.get_player_by_first_name(first_name)
    la_dict = Lakers.get_player_by_first_name(first_name)
    bk_dict= Brooklyn.get_player_by_first_name(first_name)
    
    players_list = check_length(mavs_dict, la_dict, bk_dict)
    
    if not players_list:
        response = Response("There is no player with that first name.", status=200,
                                     mimetype='application/json')
        return response
    else:   
        return jsonify({'First Name' : players_list})
                 

@app.route('/all/search/position/<string:pos>', methods=['GET'])
def get_player_by_position(pos):
    players_list = []
    
    mavs_dict = Mavericks.get_player_by_pos(pos)
    la_dict = Lakers.get_player_by_pos(pos)
    bk_dict= Brooklyn.get_player_by_pos(pos)
    players_list = check_length(mavs_dict, la_dict, bk_dict)
    
    if not players_list:
        response = Response("There is no position with that name.", status=200,
                                     mimetype='application/json')
        return response
    else:    
        return jsonify({'Position' : players_list})


@app.route('/all/search/accomplishments/<string:information>', methods=['GET'])
def get_player_by_accomplishment(information):
    players_list = []
    
    mavs_list = Mavericks.get_player_by_accomp(information)
    lakers_list = Lakers.get_player_by_accomp(information)
    bk_list = Brooklyn.get_player_by_accomp(information)

    players_list = check_length(mavs_list, lakers_list, bk_list)
      
    if not players_list:
        response = Response("There is either no player with that accomplishment \
                            or there is not accomplishment with that name.", status=200,
                                     mimetype='application/json')
        return response
    else: 
        return jsonify({'Accomplishments' : players_list}) 
    
@app.route('/help', methods=['GET'])
def get_help():
    return jsonify( {'Information': [{'Available URLs': URLS_LIST}, 
                                     {'More Info' : 'https://github.com/stobinaator/Multiple-DBs'}]})

def check_length(mavs, la, bk):
    players_list = []
    if mavs != 0:
        players_list.append(mavs)
    if la != 0:
        players_list.append(la)
    if bk != 0:
        players_list.append(bk)  
        
    return players_list

if __name__ == '__main__':
    app.run(port=1234, debug=True)