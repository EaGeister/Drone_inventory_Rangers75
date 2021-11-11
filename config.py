import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))

# Give access to the project in  ANY OS we find oursleves in
# Allow outside files/folders to be added to the project
#base directory


load_dotenv(os.path.join(basedir, '.env'))

class Config():
    '''
    Set config variables for the flask app
    Using Enviroment variables where available
    create config variables if not done already
    
    '''

    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or "you will never guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # turn off messages for updates in sqlachemy