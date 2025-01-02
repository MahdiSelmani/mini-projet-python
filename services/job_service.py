from models.models import Job, Candidate
from utils.extensions import db
import os
from sklearn.metrics.pairwise import cosine_similarity
from utils.text_utils import *
from sentence_transformers import SentenceTransformer
import joblib
import numpy as np


def create_job(title, description, skills):
    job = Job(title=title, description=description, skills=skills)
    db.session.add(job)
    db.session.commit()
    return job

def get_active_jobs():
    return Job.query.filter_by(is_active=True).all()

def get_job_by_id(job_id):
    return db.session.get(Job, job_id)

model_sbert = SentenceTransformer('paraphrase-MiniLM-L6-v2')  
model_classification = joblib.load("./train/model_classification.joblib")
model_regression = joblib.load("./train/model_regression.joblib")
scaler = joblib.load("./train/scaler.pkl")


def evaluate_job_candidates(job_id):
    # Retrieve job posting
    job_post = Job.query.get(job_id)
    if not job_post:
        return {'error': 'Job not found'}

    # Prepare job description text
    job_text = job_post.title + " " + job_post.description + " " + job_post.skills
    processed_job_text = preprocess_text(job_text)

    # Retrieve candidates for the job
    candidates = Candidate.query.filter_by(job_id=job_id).all()
    if not candidates:
        return {'error': 'No candidates found for this job'}

    # Embed the job description using SBERT
    job_embedding = model_sbert.encode([processed_job_text])[0]

    candidate_scores = []
    for candidate in candidates:
        # Process resume
        resume_path = os.path.abspath(os.path.join('uploads', 'resumes', candidate.resume_path))
        if not os.path.exists(resume_path):
            continue

        resume_text = extract_text_from_pdf(resume_path)
        processed_resume_text = preprocess_text(resume_text)

        # Process cover letter (if available)
        cover_letter_text = ""
        if candidate.cover_letter_path:
            cover_letter_path = os.path.abspath(os.path.join('uploads', 'covers', candidate.cover_letter_path))
            if os.path.exists(cover_letter_path):
                cover_letter_text = extract_text_from_pdf(cover_letter_path)
        processed_cover_letter_text = preprocess_text(cover_letter_text)

        # Combine resume and cover letter for embedding
        combined_text = processed_resume_text + " " + processed_cover_letter_text
        candidate_embedding = model_sbert.encode([combined_text])[0]

        # Calculate cosine similarity between the job description and candidate's combined resume + cover letter
        similarity_score = cosine_similarity([job_embedding], [candidate_embedding]).flatten()[0]
        skills_number = extract_skills(combined_text, job_post.skills)
        number_of_years = candidate.experience

        # Use the trained model for eligibility prediction based on features
        # Example input data for a candidate (years_of_experience, similarity, skills)
        candidate_data = np.array([[skills_number, number_of_years, similarity_score]])

        # Scale the input data using the same scaler used during training
        scaled_data = scaler.transform(candidate_data)

        # Make the eligibility prediction
        eligibility_prediction = model_classification.predict(scaled_data)

        # Map eligibility prediction to string
        eligibility = 'Eligible' if eligibility_prediction == 1 else 'Not Eligible'

        # Make the salary prediction using the regression model
        salary_prediction = model_regression.predict(scaled_data)

        # Append the candidate's details, similarity score, eligibility, and salary
        candidate_scores.append({
            'name': candidate.name,
            'email': candidate.email,
            'years': number_of_years,
            'skills': skills_number,
            'score': round(similarity_score * 100, 2),
            'eligibility': eligibility,
            'predicted_salary': round(salary_prediction[0], 2)  # Predicted salary in your desired unit
        })

    # Sort candidates by their similarity scores in descending order
    candidate_scores.sort(key=lambda x: x['score'], reverse=True)
    
    # Calculate average score
    total_score = sum(candidate['score'] for candidate in candidate_scores)
    average_score = total_score / len(candidate_scores)

    # Calculate eligible count
    eligible_candidates = sum(1 for candidate in candidate_scores if candidate['eligibility'] == 'Eligible')

    return {
        'job_name': job_post.title,
        'candidate_scores': candidate_scores,
        'average_score': round(average_score, 2),
        'eligible_candidates': eligible_candidates
    }

