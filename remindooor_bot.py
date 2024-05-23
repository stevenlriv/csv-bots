import time
import json
from config import bot_files, bot_scheduler

# Load Bot Configuration from a JSON file
with open('./config/remindooor_bot.json', 'r') as file:
    config = json.load(file)

# Lets setup the messages
header, csv_rows = bot_files.read_csv("./csv/remindooor_bot.csv")
for row in csv_rows:
    # Vars: Json Config, Day, Time, Time Zone, Message, Tag
    bot_scheduler.remindor(config['mattermost'], row[0], row[1], row[2], row[3], row[4])

# Run the bot!
while True:
    # Lets run the schedules
    bot_scheduler.run()
    
    # Sleep
    time.sleep(10)