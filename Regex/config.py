class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "-!"
    
    # OPTIONAL
    SUDO_USERS = [642191066]  # List of id's (not usernames) for users which have sudo access to the bot.   

class Development(Config):
    LOGGER = True
