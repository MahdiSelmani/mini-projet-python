from flask import Blueprint, render_template, request, jsonify
from models.models import Job, Candidate
from services.job_service import *

job_bp = Blueprint('job', __name__)

@job_bp.route('/jobs', methods=['GET'])
def show_jobs():
    jobs = get_active_jobs()
    return render_template('userjobs.html', jobs=jobs)

@job_bp.route('/rh//jobs', methods=['GET'])
def show_jobs_rh():
    jobs = get_active_jobs()
    return render_template('rhjobs.html', jobs=jobs)

@job_bp.route('/addjob', methods=['GET'])
def addjob():
    return render_template('addJob.html')

@job_bp.route('/add-job', methods=['POST'])
def add_job():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    skills = data.get('skills')

    if not title or not description or not skills:
        return jsonify({'error': 'All fields are required'}), 400

    job = create_job(title, description, skills)
    return jsonify({'message': 'Job posted successfully', 'job_id': job.id})
# Endpoint to get a job post and render an HTML page

@job_bp.route('/get-job/<int:job_id>', methods=['GET'])
def get_job(job_id):
    job_post = get_job_by_id(job_id)  # Correctly calling the service function
    if not job_post:
        return jsonify({'error': 'Job not found'}), 404
    # Render the apply.html template and pass the data
    return render_template('apply.html', 
                           job_id=job_post.id,  # Ensure this is sourced correctly from the job object
                           title=job_post.title,
                           description=job_post.description,
                           skills=job_post.skills)  # Pass as needed

@job_bp.route('/evaluate/<int:job_id>', methods=['GET'])
def evaluate_candidates(job_id):
    # Call the service to handle the evaluation logic
    result = evaluate_job_candidates(job_id)

    if 'error' in result:
        return jsonify({'error': result['error']}), 404

    # Render the evaluation results
    return render_template(
        'evaluate_candidates.html',
        job_id=job_id,
        job_name=result['job_name'],
        candidates=result['candidate_scores'],
        eligible_count = result['eligible_candidates'],
        average_score = result['average_score']
    )