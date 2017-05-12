from notify.sdk.codexbot_sdk import CodexBot
from notify.sdk.lib.rabbitmq import send_message_v3

class Notify:

    def __init__(self):
        self.sdk = CodexBot('notify', 'notify', 'localhost', '1337')
        self.sdk.log("Notify module inited")
        self.sdk.start_server()

notify = Notify()