import json
from ..lib.logging import Logging


class API:

    def __init__(self, broker, plugin_name):

        self.plugin_name = plugin_name
        self.broker = broker
        self.logging = Logging()

    def send(self, command, payload):

        data = json.dumps({'token': self.plugin_name,
                           'command': command,
                           'payload': payload})
        self.broker.send(data)

    def initialize_plugin(self, queue_name, host, port):

        payload = {
            'name': self.plugin_name,
            'queue': queue_name,
            'host': host,
            'port': port
        }

        self.send('initialize app', payload)

    def commands(self):
        pass
