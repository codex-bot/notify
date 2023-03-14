from sdk.codexbot_sdk import CodexBot
from settings import APPLICATION_TOKEN, APPLICATION_NAME, DB, SERVER, RABBITMQ

from commands.help import CommandHelp
from commands.start import CommandStart
from events.message import EventMessage


class Notify:

    def __init__(self):

        self.sdk = CodexBot(APPLICATION_NAME, SERVER['host'], SERVER['port'], db_config=DB, rabbitmq_url=RABBITMQ, token=APPLICATION_TOKEN)

        self.sdk.log("Notify module initialized: v1.17.1")

        self.sdk.register_commands([
            ('notify', 'Send notifications to your chat easily.', CommandStart(self.sdk)),
            ('notify_help', 'help', CommandHelp(self.sdk)),
            ('notify_start', 'start', CommandStart(self.sdk))
        ])

        self.sdk.set_routes([
            ('POST', '/u/{user_token}', self.notify_route_handler)
        ])

        self.sdk.start_server()

    ##
    # Route /u/{user_token} handler
    ##
    @CodexBot.http_response
    async def notify_route_handler(self, request):
        """
        :param request: - request data:
            - text
            - post
            - json
            - params - should contain {user_token}
        :return:
        """

        result = await EventMessage(self.sdk)(request)

        # Response
        return result


if __name__ == "__main__":
    notify = Notify()
