import string
from dudebot import ai


class Ping(ai.BotAI):
    """Respond to ping (and only ping) with pong."""

    def respond(self, sender_nickname, message):
        if message == 'ping':
            return 'pong'
        else:
            return None


class Echo(ai.BotAI):
    """Echos everything after the beginning 'echo'."""

    @ai.message_must_begin_with_prefix('echo')
    def respond(self, sender_nickname, message):
        return message


class EchoToNickname(ai.BotAI):
    """Using the decorator, only echo if directly by nickname."""

    @ai.message_must_begin_with_nickname
    def respond(self, sender_nickname, message):
        return message


class ROT13(ai.BotAI):

    @ai.message_must_begin_with_prefix('rot13')
    def respond(self, sender_nickname, message):
        rot13 = string.maketrans(
            "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
            "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
        )
        return string.translate(message, rot13)

