from flask import Flask
import socket
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to our website'

@app.route('/name')
def name():
    return 'Devops Rajesh'

@app.route('/ip')
def ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
