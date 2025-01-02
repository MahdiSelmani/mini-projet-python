from models.models import Candidate
from utils.extensions import db

def apply_for_job(name, email, job_id, resume_path, cover_letter_path, experience):
    candidate = Candidate(name=name, email=email, job_id=job_id, resume_path=resume_path, cover_letter_path=cover_letter_path, experience=experience)
    db.session.add(candidate)
    db.session.commit()
    return candidate
