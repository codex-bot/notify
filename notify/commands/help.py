from .base import CommandBase


class CommandHelp(CommandBase):

    async def __call__(self, payload):
        self.sdk.log("/help handler fired with payload {}".format(payload))
        await self.sdk.send_text_to_chat(
            payload["chat"],
            "Send notifications to chat easily "
            "One step integration. \n\n "
            "/notify_start — show webhook link for this chat"
        )
