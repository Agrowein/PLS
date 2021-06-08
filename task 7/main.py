from flask import Flask, render_template, request
from controllers import *
import argparse

namespace = None

app = Flask(__name__)
controller = Controller()


@app.route('/', methods=['post', 'get'])
def index():
    if request.method == 'POST':
        phone = request.form.get('phone')
        return controller.execute(phone)

    return controller.index()



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str)
    parser.add_argument('--port', type=int)
    namespace = parser.parse_args()

    app.run(host=namespace.host, port=namespace.port)
