import asyncio


class CommandBase:

    def __init__(self, sdk):
        self.sdk = sdk


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
