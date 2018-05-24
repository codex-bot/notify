from .base import EventBase
from config import CHATS_COLLECTION_NAME

class EventMessage(EventBase):

    async def __call__(self, request):

        self.sdk.log('Notification accepted {}'.format(request['text']))

        # Check for route-token passed
        if 'user_token' not in request['params']:
            self.sdk.log("Notify route handler: user_token is missed")
            return {
                'status': 404
            }

        # Check for post parameter 'message'
        if 'message' not in request['post']:
            self.sdk.log("Notify route handler: param 'message' missed")
            return {
                'text': "Error: param «message» is missed"
            }

        message = request['post']['message']
        parse_mode = request['post'].get('parse_mode', None)
        disable_web_page_preview = self.__str2bool(request['post'].get('disable_web_page_preview', "false"))
        user_token = request['params']['user_token']

        # Get user data from DB by user token
        registered_chat = self.sdk.db.find_one(CHATS_COLLECTION_NAME, {'user': user_token})

        # Check if chat was registered
        if not registered_chat or 'chat' not in registered_chat:
            self.sdk.log("Notify route handler: wrong user token passed")
            return {
                'status': 404
            }

        # Send notification
        await self.sdk.send_text_to_chat(registered_chat['chat'], message, parse_mode, disable_web_page_preview)
        return {
            'text': 'OK!'
        }

    @staticmethod
    def __str2bool(v):
        return v.lower() in ("yes", "true", "1")
