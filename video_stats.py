import requests
import json

import os 
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

YOUR_API_KEY = os.getenv("API_KEY")

Channel_Handle = 'MrBeast'

def get_playlistid():

    try:

        url = f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={Channel_Handle}&key={YOUR_API_KEY}'

        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        #print(json.dumps(data,indent = 4))

        channel_items = data["items"][0]

        channel_playlistID = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]

        print(channel_playlistID)
    
        return channel_playlistID
    
    except requests.exceptions.RequestException as e:
        raise e
if __name__ == "__main__":
   # print("get_play_list_id will be executed")
    get_playlistid()
