from flask import Flask, session, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your-secret-key'

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
