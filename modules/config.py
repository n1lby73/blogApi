from dotenv import load_dotenv
from modules import app
import os

load_dotenv()

app.config["MONGO_URI"] = os.getenv('MONGO_URI')
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
