from utils.extensions import db

class Candidate(db.Model):
    __tablename__ = 'candidate'  # Specify the table name explicitly
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    resume_path = db.Column(db.String(255), nullable=False)
    cover_letter_path = db.Column(db.String(255), nullable=True)
    experience = db.Column(db.Integer, nullable=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    job = db.relationship('Job', backref=db.backref('candidates', lazy=True))  # Corrected backref name to 'candidates'

    def __repr__(self):
        return f'<Candidate {self.name}>'

class Job(db.Model):
    __tablename__ = 'job'  # Specify the table name explicitly
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    skills = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)  # Adding is_active column

    def __repr__(self):
        return f'<Job {self.title}>'
