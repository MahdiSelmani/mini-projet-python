import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_resume_file(resume):
    if not allowed_file(resume.filename):
        raise ValueError("Invalid file type")

    filename = secure_filename(resume.filename)
    resume.save("uploads/resumes/"+filename)
    return filename

def save_cover_letter(letter):
    if not allowed_file(letter.filename):
        raise ValueError("Invalid file type")

    filename = secure_filename(letter.filename)
    letter.save("uploads/covers/"+filename)
    return filename