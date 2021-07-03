import os
import logging
import argparse
import discord

from configparser import ConfigParser

global log

SETTINGS_FILE = "settings.ini"
DEFAULT_TOKEN = '"Replace this text with your token (quotes too)"'
VERBOSE_DEBUG = True

client = discord.Client()


def main(args):
    """
    """
    settings_check = check_settings_file()
    if settings_check[0]:
        log.error("Program can't continue without settings file.")
    else:
        settings_innit_aborted = token_settings_file(settings_check[1], args.token)


def initialize_logger(verbose):
    """
    Initialize logger, standard among codes.
    Returns logging object.
    """

    logger = None       # Store the logger object and makes logs.
    fh = None           # File handler.
    ch = None           # Console handler.
    formatter = None    # Format of the output.

    try:
        os.remove("debug.log")
    except:
        pass
    
    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("debug.log")
    fh.setLevel(logging.DEBUG)

    if verbose:
        if VERBOSE_DEBUG:
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
        else:
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
    else:
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)
    print(type(logger))
    return logger


def parse_arguments():
    """
    Parse terminal arguments.
    Current args:
        -h/--help
        -t/--token "token"
    """
    #Parser help
    parser = argparse.ArgumentParser(description="UsuBot for Discord.")

    #Verbose
    parser.add_argument('-v',
                        '--verbose',
                        help="It will show all the logs on console. Useful ona development environment.",
                        action="store_true"
                        )

    #Token argument
    parser.add_argument('-t',
                        '--token',
                        help="Specify token to use on the bot, only needed one time as it will " + 
                             "save on the '" + SETTINGS_FILE + "' file. It will overwrite " +
                             "currently saved token.",
                        action="store",
                        default=DEFAULT_TOKEN
                        )

    #Read args
    return parser.parse_args()


def check_settings_file():
    """
    Check if the settings file exists. Tries to create a new one if not. It will handle
    permission error.

    Returns a tuple with information, if 'aborted' = True, the file won't exist and the code
    wouldn't be able to continue. If 'new_file' = True, the contents of the file will be empty, so
    it will need to be initialized.
    """

    aborted = False
    new_file = False

    #Check if file exists. If not, try to create it.
    if os.path.exists(SETTINGS_FILE):
        log.debug("'"+ SETTINGS_FILE + "' found.")
    else:
        log.debug("'"+ SETTINGS_FILE + "' not found.")
        try:
            open(SETTINGS_FILE, 'a').close()
            new_file = True
            log.info("'"+ SETTINGS_FILE + "' created.")
        except PermissionError:
            log.error("Permission error. Aborting...")
            aborted = True

    #Return the results.
    return (aborted, new_file)
    

def token_settings_file(new_file:bool, token):
    """
    Populate the setting with the bot section and the token attribute. It will take the argument
    string for an empty file and for a non empty file if the argument is not the default one.
    """
    abort = False
    config = ConfigParser()

    config.read(SETTINGS_FILE)

    #Set default new setting file.
    if new_file:
        config.add_section('bot')
        config.set('bot', 'token', token)
    
    #If the token from args is not the default string, it will be applied to the settings file.
    if token != DEFAULT_TOKEN:
        #Check if the section exists to avoid exceptions.
        if config.has_section('bot'):
            config.set('bot', 'token', token)
        else:
            config.add_section('bot')
            config.set('bot', 'token', token)
    
    #If the token now on the settings file is the default one, the program can't continue.
    if config['bot']['token'] == DEFAULT_TOKEN:
        abort = True
        log.error("Please, add the token on the 'settings.ini' file or with the flag '-t, --token'." +
                  " For more information, please check the help '-h, --help' page.")

    with open(SETTINGS_FILE, 'w') as f:
        config.write(f)
    
    return abort
    

if __name__ == "__main__":
    args = parse_arguments()
    log = initialize_logger(args.verbose)
    log.debug("Arguments parsed and logger initialized.")
    main(args)
    
