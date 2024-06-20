function iniciarTimer(e, pos, intervals) {
     if (e.key === 'a' && !intervals.x)
          intervals.x = setInterval(() => {
               pos.x -= 5;
               sock.volatile.emit('move.x', pos.x);
          }, 30);
     if (e.key === 'd' && !intervals.x)
          intervals.x = setInterval(() => {
               pos.x += 5;
               sock.volatile.emit('move.x', pos.x);
          }, 30);
     if (e.key === 's' && !intervals.y)
          intervals.y = setInterval(() => {
               pos.y += 5;
               sock.volatile.emit('move.y', pos.y);
          }, 30);
     if (e.key === 'w' && !intervals.y)
          intervals.y = setInterval(() => {
               pos.y -= 5;
               sock.volatile.emit('move.y', pos.y);
          }, 30);
}

function detenerTimer(e, intervals) {
     if (e.key === 'a' && intervals.x) {
          clearInterval(intervals.x);
          intervals.x = null;
     }
     if (e.key === 'd' && intervals.x) {
          clearInterval(intervals.x);
          intervals.x = null;
     }
     if (e.key === 's' && intervals.y) {
          clearInterval(intervals.y);
          intervals.y = null;
     }
     if (e.key === 'w' && intervals.y) {
          clearInterval(intervals.y);
          intervals.y = null;
     }
}
