from flask import Blueprint, request, jsonify
from services.candidate_service import apply_for_job
from utils.file_utils import save_resume_file, save_cover_letter
from models.models import Candidate
import os

candidate_bp = Blueprint('candidate', __name__)
UPLOAD_FOLDER = 'uploads/resumes'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('uploads/covers', exist_ok=True)


@candidate_bp.route('/apply', methods=['POST'])
def apply():
    if 'resume' not in request.files:
        return jsonify({'error': 'Resume file is required'}), 400

    resume = request.files['resume']
    if resume.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    cover_letter = request.files['cover_letter']
    cover_letter_path=None
    if cover_letter != '':
            cover_letter_path = save_cover_letter(cover_letter)
    resume_path = save_resume_file(resume)
    name = request.form.get('name')
    email = request.form.get('email')
    job_id = request.form.get('job_id')
    experience = request.form.get('experience')

    if not name or not email or not job_id:
        return jsonify({'error': 'All fields are required'}), 400

    candidate = apply_for_job(name, email, job_id, resume_path, cover_letter_path, experience)
    return jsonify({'message': 'Application submitted successfully', 'candidate_id': candidate.id})
