import time
import json
from config import bot_files, bot_scheduler

# Load Bot Configuration from a JSON file
with open('./config/checky_bot.json', 'r') as file:
    config = json.load(file)

# Lets setup the endpoints to check
header, csv_rows = bot_files.read_csv("./csv/checky_bot.csv")
for row in csv_rows:
    # Vars: Json Config, Endpoint Url, Every x Minute, Tag Name
    bot_scheduler.endpoint_checky(config['mattermost'], row[0], int(row[1]), row[2])

# Run the bot!
while True:
    # Lets run the schedules
    bot_scheduler.run()
    
    # Sleep
    time.sleep(10)