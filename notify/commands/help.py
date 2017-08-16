from .base import CommandBase


class CommandHelp(CommandBase):

    async def __call__(self, payload):
        self.sdk.log("/help handler fired with payload {}".format(payload))
        await self.sdk.send_text_to_chat(
            payload["chat"],
            "Send notifications to chat easily "
            "Very simple to integrate. \n\n "
            "/notify_start — show webhook for this chat"
        )
