from flask import Flask, send_from_directory
from flask_ngrok import run_with_ngrok

app = Flask(__name__, static_folder='.', template_folder='.')
run_with_ngrok(app)  # Start ngrok when app is run

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run()