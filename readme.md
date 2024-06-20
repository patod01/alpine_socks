# the socks in the alpine way

## A boring AF minigame to test SocketIO with AlpineJS. It worked!!

Features:
- player connection and desconnection handlers.
- movement handlers.
- mirroring data (number of players and movements) to everyone.
- tears and blood granted.

Hosting the game:

This command must be run in the `app` folder:
`python vale.py [dev | go] PORT`

Example:
```bash
python vale.py dev 5173
```

Resources:
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/index.html)
- [SocketIO](https://socket.io/docs/v4/)
