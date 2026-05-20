# run.py
from app import create_app, socketio

app = create_app()

if __name__ == '__main__':
    # We use socketio.run instead of app.run to enable WebSocket support
    socketio.run(app, debug=True, port=5000)