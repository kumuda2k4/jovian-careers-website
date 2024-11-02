from flask import Flask, render_template,jsonify
# Create a Flask app instance
app = Flask(__name__)
# Define a route and a view function
JOBS = [
    {
        'id':1,
        'title':'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id':2,
        'title':'Data Analyst',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id':3,
        'title':'Frontend Engineer',
        'location': 'Remote',
        'salary': 'Rs. 20,00,000'
        
    },
    {
        'id':4,
        'title':'Backend Engineer',
        'location': 'San Franciso, USA',
        'salary': '$120,000'
    },
]
@app.route('/')
def hello_jovian():
    return render_template('home.html',jobs=JOBS,company_name='Jovian' )

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

# Run the app if this file is executed
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
