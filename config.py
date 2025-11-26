import os
from dotenv import load_dotenv

# Load environment variables from the .env file into os.environ
load_dotenv()

class Config:
    """
    Central configuration class.
    Reads variables from environment variables (loaded from .env).
    """

    # Jira Configuration
    JIRA_URL = os.getenv('JIRA_URL')
    JIRA_EMAIL = os.getenv('JIRA_EMAIL')
    JIRA_API_TOKEN = os.getenv('JIRA_API_TOKEN')

    # Google Configuration
    GOOGLE_CREDENTIALS_FILE = os.getenv('GOOGLE_CREDENTIALS_FILE')
    GOOGLE_SHEET_ID = os.getenv('GOOGLE_SHEET_ID')

    # Flask Configuration
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'default-dev-key')
    DEBUG = True  # Enable debug mode for local development

    @staticmethod
    def validate_jira_config():
        """Checks if essential Jira configs are present."""
        if not all([Config.JIRA_URL, Config.JIRA_EMAIL, Config.JIRA_API_TOKEN]):
            return False, "Missing Jira configuration in .env file."
        return True, "Jira configuration loaded."