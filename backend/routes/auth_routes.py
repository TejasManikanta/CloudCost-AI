# Routes - Authentication
from flask import Blueprint, request, jsonify
from backend.auth.security import AuthService, token_required
import os
from dotenv import load_dotenv

load_dotenv()

bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@bp.route('/login', methods=['POST'])
def login():
    """User login endpoint"""
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Email and password required'}), 400
    
    email = data.get('email')
    password = data.get('password')
    
    # TODO: Verify user credentials from database
    # For now, create a test token
    user_id = 1
    token = AuthService.generate_token(user_id)
    
    return jsonify({
        'success': True,
        'token': token,
        'user_id': user_id,
        'email': email
    }), 200

@bp.route('/logout', methods=['POST'])
@token_required
def logout():
    """User logout endpoint"""
    # Token is invalidated on frontend by removing from localStorage
    return jsonify({'success': True, 'message': 'Logged out successfully'}), 200

@bp.route('/register', methods=['POST'])
def register():
    """User registration endpoint"""
    data = request.get_json()
    
    required_fields = ['email', 'password', 'first_name', 'last_name']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # TODO: Save user to database
    
    return jsonify({'success': True, 'message': 'User registered successfully'}), 201

@bp.route('/me', methods=['GET'])
@token_required
def get_current_user():
    """Get current user information"""
    user_id = request.user_id
    
    # TODO: Fetch user from database
    
    return jsonify({
        'id': user_id,
        'email': 'user@example.com',
        'first_name': 'John',
        'last_name': 'Doe'
    }), 200
