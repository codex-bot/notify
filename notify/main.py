from notify.sdk.codexbot_sdk import CodexBot


class Notify:

    def __init__(self):
        self.sdk = CodexBot('notify', 'notify', '127.0.0.1', '1337')
        self.sdk.log("Notify module initialized")
        # self.sdk.set_routes([
        #     ()
        # ])
        self.sdk.start_server()

notify = Notify()
