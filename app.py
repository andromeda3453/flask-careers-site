from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Scientist',
        'location': 'Dubai, UAE',
        'salary': 30_000
    },
    {
        'id': 2,
        'title': 'Data Engineer',
        'location': 'Abu Dhabi, UAE',
        'salary': 40_000
    },
    {
        'id': 3,
        'title': 'Data Analyst',
        'location': 'RAK, UAE',
        'salary': 35_000
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'UAQ, UAE',
        'salary': 30_000
    },
]

@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS)