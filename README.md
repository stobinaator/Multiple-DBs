# Multiple-DBs

First implementiation of multiple Databases. Trying to search for a resource, which has to be found no matter where it has been saved.

## Getting started
To install the required packages run `pip install -r requirements.txt` from the project's directory.</br>
Starting the program is as simple as running `python3 api.py`.</br>


There are 3 team rosters: Mavericks, Lakers and Brooklyn.</br>
There are 5 positions: PG, SG, SF, PF and C. </br>
There are 8 accomplishments: MVP, ROY, DPOY, Scoring, 6th, AllStar, Titles, FMVP.</br>

You can start by calling a GET request to `http://localhost/help`. It will display all available URLs.</br>

"/roster/<string:name>" can be used for GETting the whole roster or POSTing new player to a roster. <br>
"/roster/<string:name>/<int:id>" can be used for GETting or PUTting single player </br>

## Examples
1. Getting all teams that are present: `/rosters`
2. Getting specific team: `/rosters/Lakers`
3. Getting player by last name: `/all/search/last/James`
4. Getting player by first name: `/all/search/first/LeBron`
5. Getting player by accomplishment: `/all/search/accomplishments/MVP`
