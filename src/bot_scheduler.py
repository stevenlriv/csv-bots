import schedule
import bot_request
from datetime import datetime

# Run all of the bot scheduled actions
def run():
    print(datetime.now())
    schedule.run_pending()

# This loads a schedule function to send a post request and check an endpoint
# Need to provode: url, minutes between checks, tag name for scheduler
def endpoint_checky(bot_config, url, every_minutes, tag):
    schedule.every(every_minutes).minutes.do(bot_request.check_endpoint_message, bot_config, url).tag(tag)

# This loads a schedule function to send a reminder via a post request
# Its explicit and covers from Monday to Sunday with Time Zones
# Need to provode: day, time, time_zone, message, tag for scheduler
def remindor(bot_config, day, time, time_zone, message, tag):
    if day == "Monday":
        schedule.every().monday.at(time, time_zone).do(bot_request.send_message_config, bot_config, message).tag(tag)
    elif day == "Tuesday":
        schedule.every().tuesday.at(time, time_zone).do(bot_request.send_message_config, bot_config, message).tag(tag)
    elif day == "Wednesday":
        schedule.every().wednesday.at(time, time_zone).do(bot_request.send_message_config, bot_config, message).tag(tag)
    elif day == "Thursday":
        schedule.every().thursday.at(time, time_zone).do(bot_request.send_message_config, bot_config, message).tag(tag)
    elif day == "Friday":
        schedule.every().friday.at(time, time_zone).do(bot_request.send_message_config, bot_config, message).tag(tag)
    elif day == "Saturday":
        schedule.every().saturday.at(time, time_zone).do(bot_request.send_message_config, bot_config, message).tag(tag)
    elif day == "Sunday":
        schedule.every().sunday.at(time, time_zone).do(bot_request.send_message_config, bot_config, message).tag(tag)
    