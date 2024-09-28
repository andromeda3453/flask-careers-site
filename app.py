from flask import Flask, Response, render_template, request
from database import get_jobs
from forms import JobApplicationForm
import os
from utils import upload_resume

app = Flask(__name__)


@app.get("/job/<job_id>")
def job_detail(job_id):
    job = get_jobs("*", job_id)[0]
    return render_template("jobdetails.html", job=job)


@app.post("/job/<job_id>")
def submit_application(job_id):
    form = JobApplicationForm(request.form)
    if form.validate():
        file = request.files["cv"]
        file_path = os.path.join(os.getcwd(), file.filename)
        file.save(file_path)
        upload_resume(file_path)
        if os.path.exists(file_path):
            os.remove(file_path)
        return Response("submission successful", 200)

    return Response("submission unsuccessful", 400)


@app.route("/")
def home():
    jobs = get_jobs(["title", "currency", "location", "salary", "id"])
    return render_template("home.html", jobs=jobs)
