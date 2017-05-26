import random
import string
from time import time

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

        self.sdk.set_routes([
            ('POST', '/notify/{chat_token}', self.notify_route_handler)
        ])

        self.sdk.start_server()

    #
    #
    # HELP
    # todo: move to the class
    #

    async def help(self, payload):
        self.sdk.log("/help handler fired with payload {}".format(payload))
        await self.sdk.send_to_chat(
            payload["chat"],
            "Это приложение позволяет отправлять разные уведомления в чат с помощью простых запросов. "
            "И его очень просто интегрировать. \n\n "
            "/notify_start — получить ссылку для передачи сообщений в этот чат"
        )

    #
    #
    # START
    # todo: move to the class
    #

    @staticmethod
    def generate_chat_token():
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))

    """
    We will store user-to-chat linking in this collection
    _id | chat | user | dt_register
    """
    CHATS_COLLECTION_NAME = 'chats'

    async def start(self, payload):

        registered_chat = self.sdk.db.find_one(self.CHATS_COLLECTION_NAME, {'user': payload['chat']})

        if registered_chat:
            chat_token = registered_chat['chat']
        else:
            chat_token = self.generate_chat_token()
            new_chat = {
                'user': payload['chat'],
                'chat': chat_token,
                'dt_register': time()
            }
            self.sdk.db.insert(self.CHATS_COLLECTION_NAME, new_chat)
            self.sdk.log("New user registered with token {}".format(chat_token))

        message = "Адрес для отправки уведомлений в этот чат: {}/notify/{}\n\n" + \
                  "Сообщение отправляйте в POST-параметре «message»"

        await self.sdk.send_to_chat(
            payload["chat"],
            message.format(URL, chat_token)
        )

    #
    #
    # Route /notify/{chat_token} handler
    #
    #
    @CodexBot.http_response
    async def notify_route_handler(self, request):
        """
        :param request: - request data
        :               - text
        :               - post
        :               - json
        :               - params - should contain {chat_token}
        :return:
        """
        self.sdk.log('Notification accepted {}'.format(request['text']))

        # Check for route-token passed
        if 'chat_token' not in request['params']:
            self.sdk.log("Notify route handler: chat_token is missed")
            return {
                'status': 404
            }

        # Check for post parameter 'message'
        if 'message' not in request['post'] :
            self.sdk.log("Notify route handler: param 'message' missed")
            return {
                'text': "Error: param «message» is missed"
            }

        message = request['post']['message'];
        chat_token = request['params']['chat_token']

        # Get user data from DB by chat token
        registered_chat = self.sdk.db.find_one(self.CHATS_COLLECTION_NAME, {'chat': chat_token})

        # Check if chat was registered
        if not registered_chat or 'user' not in registered_chat:
            self.sdk.log("Notify route handler: wrong chat token passed")
            return {
                'status': 404
            }

        # Send notification
        await self.sdk.send_to_chat(registered_chat['user'], message)

        # Response
        return {
            'text': 'OK!'
        }

notify = Notify()
