import random
import string
from time import time
from config import URL, CHATS_COLLECTION_NAME
from .base import CommandBase


class CommandStart(CommandBase):

    async def __call__(self, payload):

        registered_chat = self.sdk.db.find_one(CHATS_COLLECTION_NAME, {'chat': payload['chat']})

        if registered_chat:
            user_token = registered_chat['user']
        else:
            user_token = self.generate_user_token()
            new_chat = {
                'chat': payload['chat'],
                'user': user_token,
                'dt_register': time()
            }
            self.sdk.db.insert(CHATS_COLLECTION_NAME, new_chat)
            self.sdk.log("New user registered with token {}".format(user_token))

        message = "Адрес для отправки уведомлений в этот чат: {}/u/{}\n\n" + \
                  "Сообщение отправляйте в POST-параметре «message»"

        await self.sdk.send_text_to_chat(
            payload["chat"],
            message.format(URL, user_token)
        )

    @staticmethod
    def generate_user_token():
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(8))