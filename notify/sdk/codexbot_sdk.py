import asyncio

from .lib.logging import Logging
from .components.broker import Broker
from .lib.server import Server
from .components.api import API
from .config import SERVER


class CodexBot:

    def __init__(self, plugin_name, queue_name, host, port):
        """
        Initiates SDK
        :param queue_name: - name of queue that this tool delegates to core
        """

        self.modules = {}

        self.logging = Logging()

        self.event_loop = asyncio.get_event_loop()

        self.broker = self.init_broker(queue_name)
        self.server = self.init_server()
        self.api = API(self.broker, plugin_name)

        self.init_queue()
        self.api.initialize_plugin(queue_name, host, port)

        self.logging.debug("Initialized")

    def init_queue(self):
        self.logging.debug("Initiate queue and loop.")
        self.broker.start()

    def init_server(self):
        return Server(self.event_loop, SERVER['host'], SERVER['port'])

    def init_broker(self, queue_name):
        return Broker(self, self.event_loop, queue_name)

    def log(self, message):
        self.logging.debug(message)

    def start_server(self):
        self.server.start()

    def set_routes(self, routes):
        self.server.set_routes(routes)

