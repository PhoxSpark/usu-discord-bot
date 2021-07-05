import logging
import discord

log = logging.getLogger('usubot')

def connect_client(token):
    """
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
    """
    async def on_ready(self):
        """
        """
        print("Logged on as {0}! Check if that's correct!".format(self.user))
    

    async def on_message(self, message):
        log.debug("{0.author}: {0.content}".format(message))

if __name__ == "__main__":
    pass