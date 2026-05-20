# app/models.py
from . import db
from datetime import datetime

class Mode(db.Model):
    """Stores the 8 unique relationship modes (Lovers, Best Friends, etc.)"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=False)
    theme_color = db.Column(db.String(20), nullable=False)
    questions = db.relationship('Question', backref='mode', lazy=True)

class Question(db.Model):
    """Stores the synchronized questions grouped by Mode"""
    id = db.Column(db.Integer, primary_key=True)
    mode_id = db.Column(db.Integer, db.ForeignKey('mode.id'), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    dimension = db.Column(db.String(50), nullable=False) # e.g., 'Trust', 'Communication'
    question_type = db.Column(db.String(50), default='multiple_choice') 
    options = db.Column(db.Text, nullable=True) # Will store JSON string of options

class Room(db.Model):
    """Temporary multiplayer rooms where two users connect"""
    id = db.Column(db.Integer, primary_key=True)
    room_code = db.Column(db.String(6), unique=True, nullable=False)
    mode_id = db.Column(db.Integer, db.ForeignKey('mode.id'), nullable=True)
    mode = db.relationship('Mode', backref='rooms')
    status = db.Column(db.String(20), default='waiting') # states: waiting, active, finished
    current_question_index = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    users = db.relationship('User', backref='room', lazy=True)

class User(db.Model):
    """Stores temporary session data for the users inside a room"""
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    aura = db.Column(db.String(20), default='purple') # NEW: Stores their avatar color
    session_id = db.Column(db.String(100), nullable=True) 
    is_ready = db.Column(db.Boolean, default=False) 
    responses = db.relationship('Response', backref='user', lazy=True)

class Response(db.Model):
    """Logs answers and calculation data for the final heatmap/results"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    answer = db.Column(db.String(500), nullable=False)
    time_taken = db.Column(db.Float, nullable=False) # To track emotional hesitation