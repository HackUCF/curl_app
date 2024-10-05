from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/curl', methods=['POST'])
def ping():
    ip = request.form.get('ip')
    command = f'curl --connect-timeout 0.1 {ip}'
    result = os.popen(command).read()
    return render_template('curl.html', curl_result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
