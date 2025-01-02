import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import fitz
from fuzzywuzzy import fuzz
import re
from datetime import datetime

# Download NLTK resources (do this once)
nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))  # Use English stopwords
    tokens = word_tokenize(text.lower())
    filtered_tokens = [
        word for word in tokens if word.isalpha() and word not in stop_words
    ]
    return ' '.join(filtered_tokens)

# Function to extract text from a resume (PDF file)
def extract_text_from_pdf(file_path):
    try:
        with fitz.open(file_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
            return text
    except Exception as e:
        return f"Error extracting text: {str(e)}"
    

def extract_skills(text, job_skills):
    """
    Extract skills from text based on job-specific skills using simple string matching.
    Returns the number of skills found.
    """
    extracted_skills = []
    for skill in job_skills.split(','):
        if skill.lower().strip() in text.lower():  # Simple comparison (case-insensitive)
            extracted_skills.append(skill.strip())
    
    # Return the number of skills found
    return len(extracted_skills)

