from notify.sdk.codexbot_sdk import CodexBot
from notify.sdk.config import DB, APPLICATION_TOKEN, URL

class Notify:

    def __init__(self):

        self.sdk = CodexBot('notifies', 'notifies', 'localhost', '1339', db_config=DB, token=APPLICATION_TOKEN)

        self.sdk.log("Notify module initialized")
        # self.sdk.set_routes([
        #     ()
        # ])

        self.sdk.register_commands([
            ('notify_help', 'help', self.help),
            ('notify_start', 'start', self.start)
        ])
        self.sdk.start_server()

    async def help(self, payload):
        self.sdk.log("/help handler fired with payload {}".format(payload))
        await self.sdk.send_to_chat(payload["chat"], "/notify_start — получить ссылку для передачи сообщений в данный чат.")


    async def start(self, payload):
        self.sdk.log("start")

        # todo: generate own user-hash and save it in DB
        user_token = payload["chat"]
        message = "Ссылка для отправки сообщений в данный чат: {}/notify/{}\n\n" + \
                  "Сообщение отправляйте в POST параметре message."

        await self.sdk.send_to_chat(
            payload["chat"],
            message.format(URL, user_token)
        )



notify = Notify()
