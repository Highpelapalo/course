from flask import Flask, request
from .bar import bar
from .foo import foo

import datetime, os

def get_my_path():
    return request.path

def get_full_path(file_name):
    return os.path.join(os.path.join(os.path.dirname((os.path.abspath(__file__))), 'logs'), file_name)

def generate_log_message(message):
    now = datetime.datetime.now() 
    return '{message} --- {time} --- {path}\n'.format(message=message, time=now.isoformat(), path=get_my_path())

def run(log_file):
    full_path = get_full_path(log_file)
    app = Flask(__name__)

    def get_my_ip():
        return request.remote_addr

    @app.route('/bar')
    def return_bar():
        with open(full_path, 'a') as fd:
            fd.write(generate_log_message('Get request for /bar from {ip}'.format(ip=get_my_ip())))
            
        return bar()

    @app.route('/foo')
    def return_foo():
        with open(full_path, 'a') as fd:
            fd.write(generate_log_message('Get request for /bar from {ip}'.format(ip=get_my_ip())))
            
        return foo()

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def handle_others(path):
        with open(full_path, 'a') as fd:
            fd.write(generate_log_message('Get request for Unhandled from {ip}'.format(ip=get_my_ip())))
        return 'Unhandled request'

    app.run(host='0.0.0.0')
    return app
