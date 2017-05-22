from notify.sdk.codexbot_sdk import CodexBot
from notify.sdk.config import DB, APPLICATION_TOKEN


class Notify:

    def __init__(self):

        self.sdk = CodexBot('notify22', 'notify', 'localhost', '1339', db_config=DB, token=APPLICATION_TOKEN)

        self.sdk.log("Notify module initialized")
        # self.sdk.set_routes([
        #     ()
        # ])

        self.sdk.register_commands([
            ('notify_help', 'help', self.help),
            ('notify_start', 'start', self.start)
        ])
        self.sdk.start_server()

    def help(self, payload):
        self.sdk.log("help")

    def start(self, payload):
        self.sdk.log("start")


notify = Notify()
