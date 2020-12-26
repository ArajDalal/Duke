# install virtual environment - python3 -m venv \Python
# activate the virtual environment - . bin/activate
# flask install - pip3 install Flask
# run some flask commands
# export FLASK_APP=Lecture_254_.py
# flask run
# debug mode on
# export FLASK_ENV=development
# flask run

# render_template - template from flask, will look into a templates named folder
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
import csv

# portfolio building
@app.route('/')
def my_home():
    return render_template('index-my.html')

@app.route('/index.html')
def my_index():
    return render_template('index-my.html')

@app.route('/<string:page_name>')
def my_works(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode ='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file=database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='',mode ='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer=csv.writer(database2,delimiter=',',quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'some error'
    else:
        return'something went wrong'