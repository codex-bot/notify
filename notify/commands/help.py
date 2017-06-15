from .base import CommandBase


class CommandHelp(CommandBase):

    async def __call__(self, payload):
        self.sdk.log("/help handler fired with payload {}".format(payload))
        await self.sdk.send_text_to_chat(
            payload["chat"],
            "Это приложение позволяет отправлять разные уведомления в чат с помощью простых запросов. "
            "И его очень просто интегрировать. \n\n "
            "/notify_start — получить ссылку для передачи сообщений в этот чат"
        )
