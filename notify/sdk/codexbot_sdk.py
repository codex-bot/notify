import asyncio

from notify.sdk.lib.db import Db
from .lib.logging import Logging
from .components.broker import Broker
from .lib.server import Server, http_response
from .config import SERVER


class CodexBot:

    # Make decorator for HTTP callback public
    http_response = http_response

    def __init__(self, application_name, queue_name, host, port, db_config, token):
        """
        Initiates SDK
        :param queue_name: - name of queue that this tool delegates to core
        """

        if not token:
            print('Please, pass your app`s token.\nYou can get it from our bot by /newapp command')
            exit()

        # Get event loop
        self.event_loop = asyncio.get_event_loop()

        self.application_name = application_name
        self.token = token

        self.logging = self.init_logging()
        self.db = self.init_db(db_config)
        self.server = self.init_server()
        self.broker = self.init_broker(application_name, queue_name)

        self.broker.start()

    def init_logging(self):
        return Logging()

    def init_server(self):
        return Server(self.event_loop, SERVER['host'], SERVER['port'])

    def init_broker(self, application_name, queue_name):
        return Broker(self, self.event_loop, application_name, queue_name)

    def init_db(self, db_config):
        self.logging.debug("Initialize db.")
        db_name = "module_{}".format(self.application_name)
        return Db(db_name, db_config["host"], db_config["port"])

    def log(self, message):
        self.logging.debug(message)

    def start_server(self):
        self.server.start()

    def set_routes(self, routes):
        self.server.set_routes(routes)

    def register_commands(self, commands):
        self.event_loop.run_until_complete(self.broker.api.register_commands(commands))

    async def send_to_chat(self, chat_hash, message):
        await self.broker.api.send('send to service', {
            "chat_hash": chat_hash,
            "text": message
        })

