# app/events.py
from flask import request
from flask_socketio import emit, join_room as socket_join_room
from . import socketio, db
from .models import Room, User
import json
from .models import Question
from .models import Room, User, Question, Response  # Added Response here

@socketio.on('join_waiting_room')
def handle_join_waiting_room(data):
    room_code = data.get('room_code')
    user_id = data.get('user_id')
    
    user = User.query.get(user_id)
    room = Room.query.filter_by(room_code=room_code).first()

    if not user or not room:
        return

    # Link the user's database record to their real-time socket session ID
    user.session_id = request.sid
    db.session.commit()

    # Place the user into the Socket.IO network room
    socket_join_room(room_code)

    # Check how many users are currently in the database for this room
    users_in_room = User.query.filter_by(room_id=room.id).all()
    
    # If two users are here, the room is full and ready to start!
    if len(users_in_room) == 2:
        room.status = 'active'
        db.session.commit()
        
        # Broadcast a message to BOTH users in the room to start the game
        emit('session_ready', {'message': 'Partner connected! Initiating sync...'}, to=room_code)

@socketio.on('request_question')
def handle_request_question(data):
    room_code = data.get('room_code')
    user_id = data.get('user_id')
    
    room = Room.query.filter_by(room_code=room_code).first()
    user = User.query.get(user_id)
    
    if not room or not user:
        return
        
    # --- THE CRUCIAL FIX IS RIGHT HERE ---
    # Put this new page's socket connection back into the specific room!
    socket_join_room(room_code)
    # -------------------------------------
        
    # Mark this specific user as ready in the database
    user.is_ready = True
    db.session.commit()
    
    # Check if BOTH users in the room are ready
    users = User.query.filter_by(room_id=room.id).all()
    if len(users) == 2 and all(u.is_ready for u in users):
        
        # Fetch the questions for whatever mode they selected
        questions = Question.query.filter_by(mode_id=room.mode_id).all()
        
        # If we still have questions left to ask...
        if room.current_question_index < len(questions):
            current_q = questions[room.current_question_index]
            
            # Reset their ready status so we can use it for locking in answers later
            for u in users:
                u.is_ready = False
            db.session.commit()
            
            # Parse the JSON string of options back into a Python list
            options = json.loads(current_q.options) if current_q.options else []
            
            # Broadcast the question to both users simultaneously
            emit('new_question', {
                'question_id': current_q.id,
                'question_text': current_q.text,
                'options': options,
                'question_type': current_q.question_type,
                'current_index': room.current_question_index + 1,
                'total_questions': len(questions)
            }, to=room_code)
        else:
            # If no questions are left, tell them the test is over
            emit('test_complete', {'message': 'Calculating your dynamic...'}, to=room_code)
@socketio.on('submit_answer')
def handle_submit_answer(data):
    room_code = data.get('room_code')
    user_id = data.get('user_id')
    question_id = data.get('question_id')
    answer = data.get('answer')
    
    room = Room.query.filter_by(room_code=room_code).first()
    user = User.query.get(user_id)
    
    if not room or not user:
        return
        
    # Save their answer to the database
    new_response = Response(
        user_id=user.id, 
        question_id=question_id, 
        answer=answer, 
        time_taken=0.0 # We will calculate actual time later
    )
    db.session.add(new_response)
    
    # Mark this user as ready (meaning they have answered)
    user.is_ready = True
    db.session.commit()
    
    # Check if BOTH users in the room have answered this question
    users = User.query.filter_by(room_id=room.id).all()
    if len(users) == 2 and all(u.is_ready for u in users):
        
        # Both answered! Advance the room to the next question
        room.current_question_index += 1
        
        # Reset ready status for the next round
        for u in users:
            u.is_ready = False
            
        db.session.commit()
        
        # Tell both browsers to trigger the "Next question loading..." animation
        emit('round_complete', to=room_code)