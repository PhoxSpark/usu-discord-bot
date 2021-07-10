import logging
import discord

log = logging.getLogger('usubot')

def connect_client(token):
    """
    Use the token and the Discord library to connect.
    """

    exit_code = 0
    client = UsuClient()

    try:
        client.run(token)
    except discord.errors.LoginFailure:
        log.error("Improper token has been passed. Please, check the token and try again.")
        exit_code = 1

    return exit_code


class UsuClient(discord.Client):
    """
    Main UsuBot class to handle features.
    """
    async def on_ready(self):
        """
        Message to show on console when ready.
        """
        print("Logged on as {0}! Check if that's correct!".format(self.user))
    

    async def on_message(self, message):
        """
        Log every message on the server connected.
        """
        log.debug("{0.author}: {0.content}".format(message))

if __name__ == "__main__":
    pass