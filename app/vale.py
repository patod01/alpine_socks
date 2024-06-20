import os, json, time, sqlite3, sys
from flask import (
     Flask, request, render_template,
     url_for, redirect, jsonify,
)
from flask_socketio import SocketIO, emit


# Flask setup #
app = Flask(
     __name__,
     static_url_path='',
     static_folder='a',
     template_folder='a'
)

app.config['SECRET_KEY'] = 'nigga'

if sys.argv[1] == 'dev':
     io = SocketIO(
          app,
          logger=True,
          async_mode=None,
          ping_interval=50,
          engineio_logger=True
     )
else:
     io = SocketIO(app, ping_interval=50)


# Default settings #
@app.errorhandler(404)
def go_default(error):
     return 'not my problem .!.', 404


### Real sh1t ###

@app.route('/')
def home():
     return render_template('a.html')

@app.route('/game')
def game():
     return render_template('index.html')


# sockets state #
sids = {}
players = {}
desconnected_players = []


@io.event
def login():

     sid = request.sid
     if desconnected_players:
          player_name = desconnected_players.pop()
          sids.update({sid: player_name})
          players[player_name]['sid'] = sid
     else:
          sids.update({sid: f'player {len(players) + 1}'})
          players.update({f'player {len(players) + 1}': {
               'sid': sid,
               'pos': [10, 20]
          }})

     print('sids:\n', sids)
     print('players:\n', players)
     print('desconnected players:\n', desconnected_players)

     emit(
          'shout_login',
          {'name': f'{sids[sid]}', 'pos': players[sids[sid]]['pos']},
          include_self = False,
          broadcast = True
     )
     return sids[sid], { player: players[player] for player in players if players[player]['sid'] }


@io.event
def testeo(msg, a='nada'):
     print(f'message: {type(msg)}, {msg}')
     print(f'valor de `a`: {a}')
     emit(
          'testeo',
          (
               f'el sucio {msg[0]}, AKA `{sids[msg[0]]}`, molesta en server.',
               f'He says `{a}, {msg[1]}...`'
          ),
          broadcast = True
     )
     # `emit`, by default, goes to the socket
     # `io.emit`, by default, goes to everyone
     return ['ho hi ho', 123], 'asdf'


@io.on('disconnect', namespace='/lobi')
def pdwarf(): pass


@io.on('disconnect')
def dwarf():
     player_name = sids.pop(request.sid)
     desconnected_players.append(player_name)
     players[player_name]['sid'] = None

     io.emit('logout', player_name)

     print('sids:\n', sids)
     print('players:\n', players)
     print('desconnected players:\n', desconnected_players)


@io.event
def pls():
     print('sids:\n', sids)
     print('players:\n', players)
     print('desconnected players:\n', desconnected_players)


@io.on('move.x')
def move_x(player_pos_x):
     players[sids[request.sid]]['pos'][0] = player_pos_x
     emit('player_moved', {
          "name": sids[request.sid],
          "pos": {
               "x": players[sids[request.sid]]['pos'][0],
               "y": players[sids[request.sid]]['pos'][1]
          }
     }, include_self=False, broadcast=True)


@io.on('move.y')
def move_y(player_pos_y):
     players[sids[request.sid]]['pos'][1] = player_pos_y
     emit('player_moved', {
          "name": sids[request.sid],
          "pos": {
               "x": players[sids[request.sid]]['pos'][0],
               "y": players[sids[request.sid]]['pos'][1]
          }
     }, include_self=False, broadcast=True)


if __name__ == '__main__':
     print('|--------------- HOOOOLAA ---------------|')
     if sys.argv[1] == 'dev':
          print('running on', sys.argv[1])
          io.run(app, host='0.0.0.0', port=int(sys.argv[2]), debug=True)
     elif sys.argv[1] == 'go':
          print('running on', sys.argv[1])
          io.run(app, host='0.0.0.0', port=int(os.getenv(
               'PORT', int(sys.argv[2])
          )))

#ned
