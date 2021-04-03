from os import environ

# To use manual values, change these
default_bot_token = "1728643400:AAGDfqiD7A7ky_p8aI6-Hps_5II3PD8aGzc"
default_sudo_chat_id =  -507324487
default_owner_id = 1461960124

# Don't change these value
bot_token = environ.get("BOT_TOKEN", default_bot_token)
sudo_chat_id = int(environ.get("SUDO_CHAT_ID", default_sudo_chat_id))
owner_id = int(environ.get("OWNER_ID", default_owner_id))
