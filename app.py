from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Scientist',
        'location': 'Dubai, UAE',
        'salary': 30_000,
        'about': 'Lorem ipsum odor amet, consectetuer adipiscing elit. Ultricies placerat arcu habitant gravida etiam praesent pulvinar tempor sollicitudin. Tincidunt suspendisse sem consectetur litora sed purus eros suscipit. Mi aenean sed rhoncus taciti, massa convallis dis. Mus vel orci conubia suscipit nibh aliquam. Tincidunt volutpat blandit sociosqu tristique eros scelerisque et rhoncus. Metus nam finibus posuere pellentesque neque; aliquet erat nascetur.',
        'company': 'Moran Instruments Ltd'
    },
    {
        'id': 2,
        'title': 'Data Engineer',
        'location': 'Abu Dhabi, UAE',
        'salary': 40_000,
        'about': 'Lorem ipsum odor amet, consectetuer adipiscing elit. Ultricies placerat arcu habitant gravida etiam praesent pulvinar tempor sollicitudin. Tincidunt suspendisse sem consectetur litora sed purus eros suscipit. Mi aenean sed rhoncus taciti, massa convallis dis. Mus vel orci conubia suscipit nibh aliquam. Tincidunt volutpat blandit sociosqu tristique eros scelerisque et rhoncus. Metus nam finibus posuere pellentesque neque; aliquet erat nascetur.',
        'company': 'Dawson Advertising Ltd'
    },
    {
        'id': 3,
        'title': 'Data Analyst',
        'location': 'RAK, UAE',
        'salary': 35_000,
        'about': 'Lorem ipsum odor amet, consectetuer adipiscing elit. Ultricies placerat arcu habitant gravida etiam praesent pulvinar tempor sollicitudin. Tincidunt suspendisse sem consectetur litora sed purus eros suscipit. Mi aenean sed rhoncus taciti, massa convallis dis. Mus vel orci conubia suscipit nibh aliquam. Tincidunt volutpat blandit sociosqu tristique eros scelerisque et rhoncus. Metus nam finibus posuere pellentesque neque; aliquet erat nascetur.',
        'company': 'Clayton Training Ltd'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'UAQ, UAE',
        'salary': 30_000,
        'about': 'Lorem ipsum odor amet, consectetuer adipiscing elit. Ultricies placerat arcu habitant gravida etiam praesent pulvinar tempor sollicitudin. Tincidunt suspendisse sem consectetur litora sed purus eros suscipit. Mi aenean sed rhoncus taciti, massa convallis dis. Mus vel orci conubia suscipit nibh aliquam. Tincidunt volutpat blandit sociosqu tristique eros scelerisque et rhoncus. Metus nam finibus posuere pellentesque neque; aliquet erat nascetur.',
        'company': 'Fleming Security Ltd'
    },
]


@app.route('/job/<job_id>')
def job_detail(job_id):
    job = next(filter(lambda x: str(x['id']) == job_id, JOBS))
    print(job)
    return render_template('jobdetails.html', job=job)

@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS)

