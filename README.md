# dudebot


## Installation

I'd strongly recommend using virtualenv (http://www.virtualenv.org).
That way once you create and activate the virtual env, you can simply add install.
```bash
pip install git+https://github.com/sujaymansingh/dudebot.git
```

## Basic usage

Let us take an example file: `bots.py`.

We can add the following.
```python
import dudebot

class Ping(dudebot.BotAI):
    def respond(self, sender_nickname, message):
        if message == "ping":
            return "pong"
```

This defines a Bot AI that will reply to any message of `ping` with `pong`.
All other messages will be ignored.

Then simply add some connection details to `bots.py`.

```python
NICKNAME = "<nickname of bot>"

PROTOCOL = "jabber"
USERNAME = "<jabber account username including @blah.com>"
PASSWORD = "<jabber account password>"

CHATROOMS = ["full chat room name (including @blah.com)"]
BOT_AIS = [
    Ping()
]
```

Now you can run the dudebot with your filename (without the `.py` extension).
```bash
python -m dudebot run bots
```

## Responding by name

The nickname of the sender is `sender_nickname`.

So add a new Bot AI to bots.py:
```python
class Hello(dudebot.BotAI):
    def respond(self, sender_nickname, message):
        if message == "hello":
            return "hello " + sender_nickname
```
and
```
BOT_AIS = [
    Ping(),
    Hello()
]
```


## Some useful decorators

There are some decorators that can be used.
```python
class Echo(dudebot.BotAI):
    @dudebot.message_must_begin_with("echo")
    def respond(self, sender_nickname, message):
        # The decorator ensures that if we reach here, then the original
        # message began with echo. Also, the decorator strips out the prefix.

        # Return everything after "echo "
        #
        return message
```

Add `Echo()` to `BOT_AIS` and run again.

Other decorators:
```python
class Attr(dudebot.BotAI):
    def __init__(self, secret_key="something"):
        self.secret_key = secret_key

    @dudebot.message_must_begin_with_attr("blah")
    def respond(self, sender_nickname, message):
        # We will only reach here if the message began with the value of
        # self.secret_key (in this case 'something')
        #
        return "unlocked " + message
```

Also, ```@dudebot.message_must_begin_with_nickname``` will make the bot AI only
respond if the message began with the bot's nickname.


## Debugging

If you want to debug without actually connecting to a server, use the `debug`
option. It will simulate a debug chatroom with some fake users.
(The bot will also be in the chatroom of course.)

```bash
$ python -m dudebot debug bots with-fake-users ed mike chris james paul
People in chatroom: ['bot', 'ed', 'mike', 'chris', 'james', 'paul']
/changeto nickname <- Changes to given nickname
Otherwise, just type to chat
(Hit enter after each line!)
ed> hi all
ed> ping
bot> pong
ed> hello
bot> hello ed
ed> echo this is a test
bot> this is a test
ed> /changeto chris
chris> hello
bot> hello chris
chris>
```

## Google Examples

There are some examples defined in `dudebot.examples.google`

Consider an example `google_examples.py`:
```python
import dudebot.examples.google

NICKNAME = "googlebot"

PROTOCOL = "doesnt matter"
USERNAME = "doesnt matter"
PASSWORD = "doesnt matter"

CHATROOMS = ["doesnt matter"]
BOT_AIS = [
    dudebot.examples.google.YoutubeSearch(),
    dudebot.examples.google.GoogleSearch()
]
```

### Google Search
```bash
$ python -m dudebot debug google with-fake-users matt
People in chatroom: ['googlebot', 'matt']
/changeto nickname <- Changes to given nickname
Otherwise, just type to chat
(Hit enter after each line!)
matt> goog.search linus torvalds
googlebot> 1 of 4
http://en.wikipedia.org/wiki/Linus_Torvalds Linus Torvalds - Wikipedia, the free encyclopedia
matt> goog.next
googlebot> 2 of 4
https://plus.google.com/%2BLinusTorvalds Linus Torvalds - Google+
matt> goog.next
googlebot> 3 of 4
http://en.wikiquote.org/wiki/Linus_Torvalds Linus Torvalds - Wikiquote
matt> goog.search asgbasijgbasipbgasijbgasojrnasorjynaoprjybarybw
googlebot> No results for asgbasijgbasipbgasijbgasojrnasorjynaoprjybarybw
matt>
```


### Youtube Search
```bash
$ python -m dudebot debug google with-fake-users matt
People in chatroom: ['googlebot', 'matt']
/changeto nickname <- Changes to given nickname
Otherwise, just type to chat
(Hit enter after each line!)
matt> yt.search benton dog deer
googlebot> 1 of 25
http://www.youtube.com/watch?v=3GRSbr0EYYU&feature=youtube_gdata JESUS CHRIST IN RICHMOND PARK: ORIGINAL UPLOAD
matt> yt.next
googlebot> 2 of 25
http://www.youtube.com/watch?v=lWv2wtvK6hg&feature=youtube_gdata Irate man chases Fenton the dog in Richmond Park
matt> yt.next
googlebot> 3 of 25
http://www.youtube.com/watch?v=Y9QurgFU7U0&feature=youtube_gdata Fenton (aka Benton) the dog catches a Deer in the big hairy forest of Richmond Park
matt>
```

