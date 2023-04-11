from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return render_template('index.html')

# @app.route('/contact')
# def contact():
#     return 'Hey my address is No 2 stadium road'


# @app.route('/services')
# def services():
#     return 'we offer web development training'

@app.route("/")
def hello_world():
    return render_template('index.html')


# @app.route('/blog')
# def blog():
#     return render_template('blog.html')

# def blog2():
#     return render_template('blog2.html')




# @app.route('/blog2.html')
# def blog2():
#     return render_template('blog2.html')

@app.route('/new.html')
def new():
    return render_template('new.html')

@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')


# @app.route('/Approval.html')
# def Approval():
#     retutn


@app.route('/message', methods=['POST', 'GET'])
def message():
    if request.method == 'POST':
        data_name = request.form['name']
        data_email = request.form['email']
        data_sub = request.form['subject']
        data_msg = request.form['message']
        with open("database.txt","a") as file:
            file.write(f'{data_name}\n')
            file.write(f'{data_email}\n')
            file.write(f'{data_sub}\n')
            file.write(f'{data_msg}\n')
            return render_template('Approval.html')
    else:
        return 'Something went wrong'

