from .base import CommandBase


class CommandHelp(CommandBase):

    async def __call__(self, payload):
        self.sdk.log("/help handler fired with payload {}".format(payload))

        self.set_bot(payload)

        await self.send(
            payload["chat"],
            "Send notifications to chat easily "
            "One step integration. \n\n "
            "/notify_start — show webhook link for this chat"
        )
