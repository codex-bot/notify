from functools import partial


class EventBase:

    def __init__(self, sdk):
        self.sdk = sdk
        self.bot = None
        self.send = partial(self.sdk.send_text_to_chat)

    def set_bot(self, payload):
        self.bot = payload.get('bot', None)
        self.send = partial(self.sdk.send_text_to_chat, bot=self.bot)
