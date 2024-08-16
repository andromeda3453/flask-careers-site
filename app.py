from flask import Flask, render_template
from database import get_jobs

app = Flask(__name__)


@app.route("/job/<job_id>")
def job_detail(job_id):
    job = get_jobs("*", job_id)[0]
    print(job)
    return render_template("jobdetails.html", job=job)


@app.route("/")
def home():
    jobs = get_jobs(["title", "currency", "location", "salary", "id"])
    return render_template("home.html", jobs=jobs)
