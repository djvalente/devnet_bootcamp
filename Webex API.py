import requests
import json

server = "https://webexapis.com/v1/"
mytoken = 'YmU3MjRmM2QtNGVlNS00YjRjLWI3MjktYjY5MmE1MWQwNGI5NjU4ZWVmYjctYjVm_P0A1_5d96674f-de50-43d7-ae6b-8071b71cb457'

def list_rooms():
    url = server + "rooms"
    headers = {
        'Authorization': f'Bearer {mytoken}', 
        'Accept': 'application/json'}

    # Send the request to the Webex API to list the rooms
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Loop through the rooms in the response and print their names and IDs
        for room in response.json()['items']:
            print(f'{room["title"]}: {room["id"]}')
    else:
        print(f'Failed to list rooms: {response.text}')

def send_message():
    url = server + "messages"
    headers = {
        'Authorization': f'Bearer {mytoken}',
        'Content-Type': 'application/json'
        }
    
    room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vOTJhYWE5ZjAtYzhkOS0xMWVkLWFhYjEtYTMzMjdhOWNiMzMy'

    message = 'Hello from india ;)'

    payload = {
        "roomId": room_id,
        "text": message
        }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print("Error sending message. Status code:", response.status_code)

# list_rooms()
send_message()