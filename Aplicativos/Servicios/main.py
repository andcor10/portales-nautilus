from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def serve_html():
    return send_from_directory('.', 'servicios.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
