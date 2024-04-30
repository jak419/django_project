import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.exceptions import ObjectDoesNotExist


class OrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Automatically accept all incoming connections
        await self.accept()

    async def disconnect(self, close_code):
        # Handling disconnecting clients
        pass

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            try:
                # Attempting to load the JSON data from the incoming message
                text_data_json = json.loads(text_data)
                message = text_data_json.get('message', 'No message provided')
                response_data = {
                    'message': f"Received message: {message}"
                }

                # Send a response back to the client
                await self.send(text_data=json.dumps(response_data))

            except json.JSONDecodeError:
                # If JSON is invalid, logging an error and possibly notify the client
                await self.send(text_data=json.dumps({
                    'error': 'Invalid JSON format.'
                }))
                print("Received invalid JSON.")
        else:
            # If text_data is None or empty, log this issue
            print("Received an empty message.")
            await self.send(text_data=json.dumps({
                'error': 'No data received.'
            }))
