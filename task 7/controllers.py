from services import Service
from flask import render_template

INDEX = 'index.html'


class Controller(object):
    def __init__(self):
        self.service = Service()

    def index(self):
        return render_template(INDEX)

    def execute(self, number):
        if number == '':
            return render_template(INDEX)

        info = self.service.find_info(number)
        return render_template(INDEX, info=info)
