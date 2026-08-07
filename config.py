import os

class Config:
    # Uses Render's secret environment variable, or falls back to our local key if offline
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    
    # Looks for Render's live database variable, or falls back to our local file if offline
    DATABASE = os.environ.get('DATABASE_URL') or os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uniroute.db')
