import json
from ..lib.logging import Logging


class API:

    def __init__(self, broker, app_name):

        self.app_name = app_name
        self.broker = broker
        self.logging = Logging()

    def send(self, command, payload):

        data = json.dumps({'token': self.app_name,
                           'command': command,
                           'payload': payload})
        self.broker.send(data)

    def initialize_app(self, queue_name, host, port):

        payload = {
            'name': self.app_name,
            'queue': queue_name,
            'host': host,
            'port': port
        }

        self.send('initialize app', payload)

    def commands(self):
        pass
