import os
from pathlib import Path
from dotenv import load_dotenv
from peewee import MySQLDatabase


env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

db = MySQLDatabase(
    os.environ["DB_NAME"],
    host=os.environ["DB_HOST"],
    port=int(os.environ["DB_PORT"]),
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    charset="utf8",)