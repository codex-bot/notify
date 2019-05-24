import asyncio
from functools import partial


class CommandBase:

    def __init__(self, sdk):
        self.sdk = sdk
        self.bot = None
        self.send = partial(self.sdk.send_text_to_chat)

    def set_bot(self, payload):
        self.bot = payload.get('bot', None)
        self.send = partial(self.sdk.send_text_to_chat, bot=self.bot)


class CommandSome:
    """
    Call several commands one after one.

    Usage example:
    > CommandSome([CommandHelp(self.sdk), CommandStart(self.sdk)])
    """

    def __init__(self, collables):
        self.callables = collables

    async def __call__(self, payload):
        await asyncio.wait([obj(payload) for obj in self.callables])
