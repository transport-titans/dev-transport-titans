from flask import Flask, render_template, request, Response
# import pyodbc

# server = 'CB-ROG-Computer\TTSQL'
# database = 'Test'

# connection_string = (
#     f'DRIVER={{ODBC Driver 17 for SQL Server}};'
#     f'SERVER={server};DATABASE={database};'
#     'Trusted_Connection=yes;'
# )


mainapp = Flask (
    __name__,
    template_folder='templates',
    static_folder='static'
    )

@mainapp.route("/")
@mainapp.route("/home")
def home():
    return render_template('HomePage.html')

@mainapp.route("/signin", methods = ['GET', 'POST'])
def signin():
    if request.method == 'POST':
        redColor = "#FF0000"
        username = request.form.get('username')
        password = request.form.get('password')
        if username == '' and password != '':
            return render_template('SignIn.html', username_error = redColor)
        elif password == '' and username != '':
            return render_template('SignIn.html', password_error = redColor, keepUsername = username)
        else:
            return render_template('SignIn.html', password_error = redColor, username_error = redColor)
    return render_template('SignIn.html')

# @mainapp.route("/signin", methods = ['GET', 'POST'])
# def signin():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         if username == '':
#             dynamic_color = '#ff0000'
#             return render_template('SignIn.html', dynamic_color = dynamic_color)
#     return render_template('SignIn.html')

# @mainapp.route('/dynamic_styles')
# def dynamic_styles():
#     dynamic_color = "#FF0000"  # Replace with your dynamic color logic
#     css_content = f".credentials::placeholder {{ color: {dynamic_color}; }}"
#     return Response(css_content, content_type='text/css')

if __name__ == '__main__':
    mainapp.run(debug=True)













    
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# uri = "mongodb+srv://cbortea:<password>@clusterfuck.jtvfwmp.mongodb.net/?retryWrites=true&w=majority"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)