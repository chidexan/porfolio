from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def home():
    return render_template('index.html')

def database(data):
    with open('database.txt', mode='a') as database:
        name = data['username']
        email = data['useremail']
        message = data['usermessage']
        file = database.write(f'\nName:{name} Email:{email} Message:{message}')
@app.route("/form", methods = ['POST', 'GET'])
def form():
    if request.method == 'POST':
        # username = request.form['username']
        # useremail = request.form['useremail']
        # usermessage = request.form['usermessage']
        data = request.form.to_dict()
        database(data)

        # if valid_form(request.form['username'], request.form['useremail'], request.form['usermessage']):
        # return f'Thank you for contacting us {username} check {useremail} for a feedback'
        return render_template('reply.html')
    else:
        error = 'You are a hacker'
        return f"{error}"
    # return render_template('form.html', error = error)


@app.route("/reply")
@app.route("/reply.html")
def feed():
    return render_template('reply.html')



@app.route("/register", methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        userlastname = request.form['userlastname']
        userdateofbirth = request.form['userdateofbirth']
        usersex = request.form['usersex']

    useremail = request.form['useremail']
    userpassword = request.form['userpassword']
    userconfirmpassword = request.form['userconfirmpassword']




    # return render_template('registration.html', username = username, userlastname= userlastname, userdateofbirth = userdateofbirth, usersex = usersex, useremail = useremail, userpassword =userpassword, userconfirmpassword = userconfirmpassword )
    # else:
    # error = 'ya mad go fin work idiot'
    # return f"{error}"


# @app.route("/registration")
# @app.route("/registration.html")
# def regform():
#     return render_template('registration.html')