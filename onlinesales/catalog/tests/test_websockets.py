from channels.testing import WebsocketCommunicator
from django.test import TestCase
from channels.routing import URLRouter
from django.urls import path
from catalog.consumers import OrderConsumer
import json


class WebSocketTestCase(TestCase):
    async def test_my_consumer(self):
        # Setup the application for testing
        application = URLRouter([
            path("ws/catalog/", OrderConsumer.as_asgi()),
        ])

        # Creating a WebsocketCommunicator instance
        communicator = WebsocketCommunicator(application, "/ws/catalog/")
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)

        # Test sending a properly formatted JSON message to the WebSocket
        test_message = {
            "message": "hello guys, marketplace is open for business"}
        await communicator.send_to(text_data=json.dumps(test_message))
        response = await communicator.receive_from()
        response_data = json.loads(response)

        # Check if the response is the expected JSON message
        self.assertEqual(response_data, {
                         "message": "Received message: hello guys, marketplace is open for business"})

        # Closing the connection
        await communicator.disconnect()
