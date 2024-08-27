from flask import Flask, render_template, request
from database import get_jobs
from forms import JobApplicationForm

app = Flask(__name__)


@app.get("/job/<job_id>")
def job_detail(job_id):
    job = get_jobs("*", job_id)[0]
    return render_template("jobdetails.html", job=job)


@app.post("/job/<job_id>")
def submit_application(job_id):
    print(request.form)
    form = JobApplicationForm(request.form)
    print(form.data)


@app.route("/")
def home():
    jobs = get_jobs(["title", "currency", "location", "salary", "id"])
    return render_template("home.html", jobs=jobs)
