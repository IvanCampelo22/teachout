import os 
from dotenv import load_dotenv

load_dotenv()


USER=os.environ.get("SQL_USER_LOCAL")
PASSWORD=os.environ.get("SQL_PASSWORD_LOCAL")
HOST=os.environ.get("SQL_HOST_LOCAL")
NAME=os.environ.get("SQL_NAME_LOCAL")
PORT=os.environ.get("SQL_PORT_LOCAL")
SECRET_KEY=os.environ.get("SECRET_TEACHEOUT")
