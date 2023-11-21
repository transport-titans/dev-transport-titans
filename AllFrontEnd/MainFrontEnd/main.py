from flask import Flask, render_template, redirect, url_for, request


usr = 'cbortea'
pwd = 'MiscaMusca123'

error_style = '#ff0000'

mainApp = Flask(
    __name__,
    template_folder = 'templates',
    static_folder = 'static'
)

@mainApp.route("/")
@mainApp.route("/home")
def HomePage():
    return render_template('HomePage.html')


@mainApp.route("/authentication", methods = ['GET', 'POST'])
def authentication():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == '' and password == '':
            dynamicErrors = 'Please enter an Username and a Password!'
            return render_template('Authentication.html', username_missing = error_style, password_missing = error_style, dynamicErrors = dynamicErrors)
        elif username == '' and password != '':
            dynamicErrors = 'Please enter an Username!'
            return render_template('Authentication.html', username_missing = error_style, dynamicErrors = dynamicErrors)
        elif username != '' and password == '':
            dynamicErrors = 'Please enter a Password!'
            return render_template('Authentication.html', password_missing = error_style, dynamicErrors = dynamicErrors, keepUsername = username)
        if username != usr or password != pwd:
            dynamicErrors = 'Incorrect Credentials!'
            return render_template('Authentication.html', dynamicErrors = dynamicErrors, keepUsername = username)
        elif username == usr and password == pwd:
            dynamicErrors = 'Success!'
            return render_template('Authentication.html', dynamicErrors = dynamicErrors)


    return render_template('Authentication.html')

@mainApp.route("/registration", methods = ['GET', 'POST'])
def registration():
    return render_template('Registration.html')

if __name__ == '__main__':
    mainApp.run(
        debug = True,
        port = '5000'
    )