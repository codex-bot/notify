import asyncio
import json
import logging

from notify.sdk.components.api import API
from notify.sdk.lib.rabbitmq import init_receiver_v3, add_message_to_queue


class Broker:

    def __init__(self, core, event_loop, application_name, queue_name):
        """
        Application broker initialization
        :param core:
        :param event_loop:
        :param queue_name: - passed from sdk constructor
        """
        logging.info("Broker started with queue_name " + queue_name)
        self.core = core
        self.event_loop = event_loop
        self.queue_name = queue_name
        self.api = API(self, application_name)

    @asyncio.coroutine
    def callback(self, channel, body, envelope, properties):
        try:
            logging.debug(" [x] Received %r" % body)
            yield from self.api.process(body.decode("utf-8"))
        except Exception as e:
            logging.error("Broker callback error: {}".format(e))

    def send(self, message, host='localhost'):

        self.event_loop.run_until_complete(add_message_to_queue(
            message, 'core'
        ))

    def start(self):
        self.event_loop.run_until_complete(init_receiver_v3(self.callback, self.queue_name))

    # def initialize_app(self, queue_name, host, port):
    #     try:
    #         token = self.core.db.find_one('configuration', {'id': 1}).get('token')
    #         self.api.token = token
    #     except:
    #         self.api.initialize_app(queue_name, host, port)

