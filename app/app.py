from flask import Flask, render_template
from flask_cors import CORS
from routes.job_routes import job_bp 
from routes.candidate_routes import candidate_bp
from utils.extensions import db

def create_app():
    app = Flask(__name__)

    # Enable Cross-Origin Resource Sharing (CORS)
    CORS(app)

    # Configure the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/recruitmentdb'  # Modify credentials if needed
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    # Create tables if they don't exist
    with app.app_context():
        db.create_all()  # This creates all tables in the database

    # Register Blueprints
    app.register_blueprint(job_bp)  # All job routes will be prefixed with /job
    app.register_blueprint(candidate_bp)  # All candidate routes will be prefixed with /candidate

    # Define route for the root URL
    @app.route('/')
    def dashboard():
        return render_template('dashboard.html')  # Render the dashboard.html template

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
