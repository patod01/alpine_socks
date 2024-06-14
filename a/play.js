function emit_test() {
     sock.emit(
          'testeo',
          [sock.id, "i'm the world"],
          'pete',
          (a1, a2) => console.log(a1, a2)
     );
}

sock.on('shout_login', (player) => {
     console.log(player.name, 'has entered the area!');
     console.log('position:', player.pos);
     Alpine.store('players').push({
          name: player.name,
          pos: {
               x: player.pos[0],
               y: player.pos[1]
          }
     });
});

sock.on('logout', (player_name) => {
     console.log(player_name, 'has chickened away..');
     Alpine.store(
          'players',
          Alpine.store('players').filter(
               ({name}) => name !== player_name
          )
     );
});

sock.on('testeo', (a, b) => console.log(a, b));

sock.on('player_moved', (player_moved) => {
     for (let player of Alpine.store('players')) {
          if (player.name == player_moved.name) {
               player.pos = player_moved.pos;
          }
     }
});
