import requests

# Sends a post message to an url endpoint
# Need to provide: Url, Bearer Token, Message and Json Data
# Returns True if succeed or false if failed
def send_message(url, token, message, data):
    # Lets set the header of the request
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json"
    }

    # Lets send the post request
    response = requests.post(url, headers=headers, json=data)

    # We analyze the response
    if response.status_code == 201:
        print("Message Sent: " + message)
        return True
    else:
        print(f"Failed to send message: {message}. Status code: {response.status_code}")
        return False

# Prepares and sends a message to an url endpoint 
# Needs to provide: Bot configuration 
# Returns True if succeed or false if failed
def send_message_config(bot_config, message):
    # Lets initiate the data dictionary
    data = {
        "channel_id": bot_config["channel_id"],
        "message": bot_config["channel_notification"] + " " + message  
    }
    if send_message(bot_config["server_url"], bot_config["bot_token"], message, data):
        return True
    else:
        return False

# Send a message after doing an endpoint check if its false
# Need to provode: bot configuration, url
# Returns True if the endpoint is up or false if down
def check_endpoint_message(bot_config, url):
    # Lets initiate the data dictionary
    data = {
        "channel_id": bot_config["channel_id"],
        "message": ""  # Initialize an empty message
    }

    # Lets Establish the message
    message = bot_config["channel_notification"] + " "   

    try:
        # Lets send the get request
        response = requests.get(url)

        # We analyze the response
        if 200 <= response.status_code < 300:
            print(f"Endpoint {url} is healthy!")
            return True
        else:
            # Lets add the failed message to the message and data variable
            message += f"Endpoint DOWN {url} returned status code: {response.status_code}"
            data["message"] = message

            # Lets print the message and send it
            print(message)
            send_message(bot_config["server_url"], bot_config["bot_token"], message, data)

            # The endpoint is down, so we return false
            return False
    except requests.exceptions.RequestException as e:
        # Lets add the failed message to the message and data variable
        message += f"Error occurred while checking endpoint {url}: {e}"
        data["message"] = message

        # Lets print the message and send it
        print(message)
        send_message(bot_config["server_url"], bot_config["bot_token"], message, data)

        # We could not check the endpoint, so we return error
        return False