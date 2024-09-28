from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
import logging


# Load env variables
load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Create DB connection
try:
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

except Exception:
    logging.error("Error while trying to establish connection to database")


def get_jobs(columns: list[str], id: int = None):
    columns = ",".join(columns)
    condition = f"Where id = {id}" if id else ""

    try:
        with engine.connect() as conn:
            result = conn.execute(text(f"select {columns} from jobs {condition} limit 3"))
            jobs = result.all()
            jobs = [row._asdict() for row in jobs]
            return jobs
    except Exception:
        logging.error("Unable to retrieve jobs data")
        return []
