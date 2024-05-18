# from flask import Flask, url_for, request, send_from_directory, render_template
# from markupsafe import escape

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if (request.method == 'GET'):
#         return render_template('103-index.html')
#     else:
#         return "Say fuck CC!"

# @app.post('/<name>')
# def theName(name):
#     return f"Fuck {escape(name)}!"
# @app.get('/hello')
# def gethello():
#     return "Fuck Anyway"

# with app.test_request_context('/hello', method='GET'):
#     assert request.path == '/hello'
#     assert request.method == 'GET'
