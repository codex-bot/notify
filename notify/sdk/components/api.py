import json

import logging

import asyncio

from ..lib.logging import Logging


class API:

    def __init__(self, broker, app_name):

        self.app_name = app_name
        self.broker = broker
        self.token = app_name
        self.db = broker.core.db
        self.logging = Logging()
        self.commands_list = {}

        # Methods list (command => processor)
        self.methods = {
            'show message': self.show_message,
            'service callback': self.service_callback
            # 'set token': self.set_token
        }

    def process(self, message_data):
        try:
            message_data = json.loads(message_data)
            payload = message_data['payload']
            command = message_data.get('command', 'show message')
            self.methods[command](payload)
        except Exception as e:
            logging.error("API Message Process error: {}".format(e))

    def send(self, command, payload):

        data = json.dumps({'token': self.broker.core.token,
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

        return self.send('initialize app', payload)

    def register_commands(self, commands):
        commands_to_send = []
        for cmd, desc, clb in commands:
            self.commands_list[cmd] = clb
            commands_to_send.append((cmd, desc))
        self.send('register commands', commands_to_send)

    # API COMMANDS

    # def set_token(self, data):
    #     try:
    #         token = data['token']
    #         conf = self.db.find_one('configuration', {'id': 1})
    #         if not conf:
    #             self.db.insert('configuration', {'id': 1, 'token': token})
    #         else:
    #             conf['token'] = token
    #             self.db.update('configuration', {'_id': conf['_id']}, {'$set': {'token': token}})
    #     except Exception as e:
    #         logging.error("Token not set. {}".format(e))
    #     else:
    #         self.token = token
    #         self.register_commands()

    def show_message(self, data):
        logging.info(data)

    def service_callback(self, data):
        self.commands_list[data['command']](data)
