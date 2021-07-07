import os
import logging

from configparser import ConfigParser

import bot
import settings_lib

from settings_lib import SettingsFile

SETTINGS_FILE = "settings.ini"
TOKEN_SECTION = "bot"
TOKEN_OPTION = "token"

log = logging.getLogger('usubot')

def start(args):
    """
    """
    exit_code = 0
    settings_file = settings_lib.SettingsFile(SETTINGS_FILE)
    settings_file.create_settings()

    if settings_file.file["exists"]:
        log.debug("Settings file exists.")
        #Check if token was specified trough args.
        if args.token != "":
            settings_file.set_data(TOKEN_SECTION, TOKEN_OPTION, args.token)
        #Check if token is empty.
        if settings_file.get_data(TOKEN_SECTION, TOKEN_OPTION) == "":
            log.error("Token not specified. Program will not continue. You can specify the token " +
                      "using the flag -t or --token or by editing the file called: '" +
                      SETTINGS_FILE + "'. Fix the issue and try again.")
        else:
            log.debug("Token not default found.")
            exit_code = bot.connect_client(settings_file.get_data(TOKEN_SECTION, TOKEN_OPTION))
    
    log.debug("Execution terminated. Exit code: " + str(exit_code))


if __name__ == "__main__":
    pass