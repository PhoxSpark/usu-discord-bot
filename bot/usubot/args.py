import argparse

def parse_arguments(settings_file = "setting.ini"):
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
                             "save on the '" + settings_file + "' file. It will overwrite " +
                             "currently saved token.",
                        action="store",
                        default=""
                        )

    #Read args
    return parser.parse_args()