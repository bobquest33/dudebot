import string
from dudebot import core


class Ping(core.BotAI):
    """Respond to ping (and only ping) with pong."""

    def respond(self, sender_nickname, message):
        if message == 'ping':
            return 'pong'
        else:
            return None


class Echo(core.BotAI):
    """Echos everything after the beginning 'echo'."""

    @core.message_must_begin_with('echo')
    def respond(self, sender_nickname, message):
        return message


class EchoToNickname(core.BotAI):
    """Using the decorator, only echo if directly by nickname."""

    @core.message_must_begin_with_nickname
    def respond(self, sender_nickname, message):
        return message


class ROT13(core.BotAI):

    @core.message_must_begin_with('rot13')
    def respond(self, sender_nickname, message):
        rot13 = string.maketrans(
            "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
            "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
        )
        return string.translate(message, rot13)

