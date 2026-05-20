# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .models import Mode, Room, User
from . import db
import random
import string
from .scoring import calculate_relationship_report
# Create a blueprint for our main routes
main = Blueprint('main', __name__)

def generate_room_code():
    """Generates a random 6-character uppercase code"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

@main.route('/')
def index():
    # Landing Page
    return render_template('index.html')

@main.route('/modes')
def mode_selection():
    # Fetch all 8 modes from the database to display on the UI
    modes = Mode.query.all()
    return render_template('mode_selection.html', modes=modes)

@main.route('/create-room', methods=['POST'])
def create_room():
    # Logic to generate a unique room
    mode_id = request.form.get('mode_id')
    user_name = request.form.get('user_name')
    aura = request.form.get('aura', 'purple') # Capture aura
    
    room_code = generate_room_code()
    new_room = Room(room_code=room_code, mode_id=mode_id, status='waiting')
    db.session.add(new_room)
    db.session.commit() # <--- This is the crucial part that was missing!
    
    # Create the host user
    host_user = User(room_id=new_room.id, name=user_name, aura=aura)
    db.session.add(host_user)
    db.session.commit()
    
    return redirect(url_for('main.waiting_room', code=room_code, user_id=host_user.id))

@main.route('/room/<code>')
def waiting_room(code):
    room = Room.query.filter_by(room_code=code).first_or_404()
    return render_template('waiting_room.html', room=room)
@main.route('/join')
def join_room_page():
    # Shows the join form to User B
    return render_template('join_room.html')

@main.route('/join-post', methods=['POST'])
def join_room_post():
    # Process User B's form submission
    room_code = request.form.get('room_code').upper()
    user_name = request.form.get('user_name')
    aura = request.form.get('aura', 'emerald') # Capture aura
    
    room = Room.query.filter_by(room_code=room_code).first()
    
    # Validation checks
    if not room:
        return "Room not found. Check the code.", 404
    
    users_in_room = User.query.filter_by(room_id=room.id).count()
    if users_in_room >= 2:
        return "Room is already full!", 400
        
    # Add User B to the database
    guest_user = User(room_id=room.id, name=user_name, aura=aura)
    db.session.add(guest_user)
    db.session.commit()
    
    # Send User B to the waiting room (which will instantly trigger the sync)
    return redirect(url_for('main.waiting_room', code=room_code, user_id=guest_user.id))

@main.route('/session/<code>')
def active_session(code):
    # This is where both users are sent once the handshake is complete
    room = Room.query.filter_by(room_code=code).first_or_404()
    user_id = request.args.get('user_id')
    return render_template('active_session.html', room=room, user_id=user_id)
@main.route('/results/<code>')
def results_page(code):
    room = Room.query.filter_by(room_code=code).first_or_404()
    user_id = request.args.get('user_id')
    current_user = User.query.get(user_id)
    
    users = User.query.filter_by(room_id=room.id).all()
    if len(users) < 2:
        return "Waiting for your partner to join the results page...", 202

    # Run the real psychological calculations using database responses
    report = calculate_relationship_report(room.id)
    
    return render_template(
        'result_dashboard.html', 
        room=room, 
        current_user=current_user,
        users=users, 
        score=report["overall_score"],
        dimensions=report["dimensions"],
        suggested_dynamic=report["suggested_dynamic"],
        user_a_insights=report["user_a_insights"],
        user_b_insights=report["user_b_insights"],
        hidden_traits=report["hidden_traits"],     # NEW
        heatmap_data=report["heatmap_data"],       # NEW
        user_a_summary=report["user_a_summary"],   # NEW
        user_b_summary=report["user_b_summary"]    # NEW
    )