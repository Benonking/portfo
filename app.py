from flask import Flask, redirect,render_template, send_from_directory, abort, request
import os
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    """Serve index page"""
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    """Serve any other page"""
    # Append .html automatically if missing
    if not page_name.endswith('.html'):
        page_name = f"{page_name}.html"

    try:
        return render_template(page_name)
    except:
        abort(404)  # return 404 page if not found


@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    '''
    Submit _data
    '''
    if request.method=='POST':
        try:

            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not savew to database'
    else:
        return ' went wrongForm submited'
    

def write_to_csv(data):
    fieldnames = ['email', 'subject', 'message']
    file_exists = os.path.isfile('./database.csv')

    with open('./database.csv', mode='a', newline='') as db:
        writer = csv.DictWriter(db, fieldnames=fieldnames)

        # Write header only if the file is new
        if not file_exists:
            writer.writeheader()

        writer.writerow(data)

def write_to_file(data):
    with open('./templates/database.txt',mode='a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = db.write(f'\n{email}, {subject}, {message}')
