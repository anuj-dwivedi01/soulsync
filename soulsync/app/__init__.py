# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
import os

# Initialize extensions globally so they can be imported elsewhere
db = SQLAlchemy()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'soulsync_super_secret_key' # We'll secure this later
    
    # Configure SQLite database location
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'soulsync.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Bind extensions to the app
    db.init_app(app)
    # cors_allowed_origins="*" allows clients to connect from anywhere during development
    socketio.init_app(app, cors_allowed_origins="*")

    # Import models here to avoid circular imports
    from . import models

    # Automatically create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    from .routes import main
    app.register_blueprint(main)
    from . import events
    return app