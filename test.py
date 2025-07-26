from flask import Flask, render_template, request
import os, subprocess
import base64

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    # append encode code
    string_to_encode = request.form['dec_input'].encode('utf-8')
    output = base64.b64encode(string_to_encode).decode('utf-8')
    return output

@app.route('/decode', methods=['POST'])
def decode():
    # append decode code

    string_to_decode = request.form['enc_input'].encode('utf-8')
    output = base64.b64decode(string_to_decode).decode('utf-8')
    return output

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

