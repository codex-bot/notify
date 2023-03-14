import random
import string
from time import time
from settings import URL, CHATS_COLLECTION_NAME, RANDOM_TOKEN_LEN
from .base import CommandBase


class CommandStart(CommandBase):

    async def __call__(self, payload):

        self.set_bot(payload)

        registered_chat = self.sdk.db.find_one(CHATS_COLLECTION_NAME, {'chat': payload['chat'], 'bot': self.bot})

        if registered_chat:
            user_token = registered_chat['user']
        else:
            user_token = self.generate_user_token()
            new_chat = {
                'chat': payload['chat'],
                'user': user_token,
                'dt_register': time(),
                'bot': self.bot
            }
            self.sdk.db.insert(CHATS_COLLECTION_NAME, new_chat)
            self.sdk.log("New user registered with token {}".format(user_token))

        message = "Use this webhook for sending notifications to the chat:\n" \
                  "\n" \
                  "<code>{}/u/{}</code>\n" \
                  "\n" \
                  "Make a POST request with text in «message» param."

        await self.send(
            payload["chat"],
            message.format(URL, user_token),
            "HTML"
        )

    @staticmethod
    def generate_user_token():
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(RANDOM_TOKEN_LEN))
