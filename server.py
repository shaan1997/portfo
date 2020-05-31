from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)

@app.route('/<page_name>')
def hello_world(page_name):
    return render_template(page_name)

@app.route('/')
def works():
    return render_template('index.html')

def database(data):
    with open('database.txt',mode='a') as database:
        email = data["email"]
        subject = data['subject']
        message = data['message']
        database.write(f'\n {email} {subject} {message}')

def write_to_csv(data):
    with open('database.csv',mode='a',newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer= csv.writer(database2,delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/simple_form', methods=['POST', 'GET'])
def simple_form():
    if request.method== 'POST':
        data = request.form.to_dict()
        database(data)
        write_to_csv(data)
        return redirect('thankyou.html')

    else:
        return 'something went wrong'

