import os
from dotenv import load_dotenv
from nio import AsyncClient, AsyncClientConfig, LoginError, RoomSendResponse, KeyVerificationEvent
import asyncio
load_dotenv()

# Replace these with your saved session info
homeserver = 
user_id = 
access_token = 
device_id =   # Optional if you want to re-use the device ID
room_id = 
message_content = "Hello, Matrix!"


async def main():
    # Initialize the client with access token
    config = AsyncClientConfig(encryption_enabled=True)
    client = AsyncClient(homeserver, user=user_id, config=config)
    client.access_token = access_token
    # Log in to get the access token and device ID
    try:
        print("Logged in successfully")
        print("Access token:", client.access_token)
        print("Device ID:", client.device_id)

        # Optionally, join the room if not already a member
        await client.join(room_id)

        # Send a message to the room
        send_response = await client.room_send(
            room_id=room_id,
            message_type="m.room.message",
            content={
                "msgtype": "m.text",
                "body": message_content,
            }
        )

        # Check if the message was sent successfully
        if isinstance(send_response, RoomSendResponse):
            print("Message sent successfully!")
        else:
            print("Failed to send message:", send_response)

    finally:
        await client.close()

asyncio.run(main())
