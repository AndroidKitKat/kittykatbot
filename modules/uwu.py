#!/usr/bin/env python

import random

NAME    = 'owo'
ENABLE  = True
PATTERN = '^(?P<target>).*'
IGNORE  = ('gonzobot', 'kittykatbot')

def command(bot, nick, message, channel, target=None):
  if nick == "gonzobot" or nick == "kittykatbot":
    return

    if 'uwu' in target:
        response = 'owo'
    elif 'UwU' in target:
        response = 'OwO'
    elif 'UWU' in target:
        response = 'OWO'
    elif: 'uWu' in target:
        response = 'oWo'
    elif 'owo' in target:
        response = 'uwu'
    elif 'OwO' in target:
        response = 'UwU'
    elif 'OWO' in target:
        response = 'UWU'
    elif 'oWo' in target:
        reponse = 'uWu'

  bot.send(channel, nick, response)

def register(bot):
 return ((PATTERN, command),)
