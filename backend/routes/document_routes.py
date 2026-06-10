# Routes - Documents
from flask import Blueprint, request, jsonify
from backend.auth.security import token_required
from datetime import datetime
import os

bp = Blueprint('documents', __name__, url_prefix='/api/documents')

ALLOWED_EXTENSIONS = {'pdf', 'docx', 'xlsx', 'csv', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/upload', methods=['POST'])
@token_required
def upload_document():
    """Upload and analyze a document"""
    user_id = request.user_id
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400
    
    # TODO: Save file and analyze with NLP
    filename = file.filename
    
    return jsonify({
        'success': True,
        'file_id': 1,
        'filename': filename,
        'uploaded_at': datetime.now().isoformat()
    }), 201

@bp.route('/<int:file_id>', methods=['GET'])
@token_required
def get_document(file_id):
    """Get document details"""
    user_id = request.user_id
    
    # TODO: Fetch document from database
    
    return jsonify({
        'id': file_id,
        'filename': 'document.pdf',
        'uploaded_at': datetime.now().isoformat()
    }), 200

@bp.route('/<int:file_id>/extract', methods=['GET'])
@token_required
def get_extracted_data(file_id):
    """Get extracted data from document"""
    user_id = request.user_id
    
    # TODO: Fetch extracted requirements from database
    
    return jsonify({
        'file_id': file_id,
        'extracted_data': {
            'project_name': 'Sample Project',
            'requirements': {}
        }
    }), 200

@bp.route('/<int:file_id>', methods=['DELETE'])
@token_required
def delete_document(file_id):
    """Delete a document"""
    user_id = request.user_id
    
    # TODO: Delete document from database
    
    return jsonify({'success': True, 'message': 'Document deleted'}), 200
