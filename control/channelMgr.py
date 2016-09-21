# -*- coding: utf-8 -*-

from utils import myglobals
from utils import filemanager


def loadChannels():
    myfile = filemanager.MyFile('channels', True, True, True)
    myglobals.CHANNELS = myfile.read_lines()


def Check2Save(channel):
    if myglobals.CHANNELS:
        if channel not in myglobals.CHANNELS:
            saveChannel(channel, False, True)
    else:
        saveChannel(channel, True, False)


def saveChannel(channel, write, append):
    myfile = filemanager.MyFile('channels', False, write, append)
    myfile.write_line(str(channel) + "\n")


def sayHello2Channels(bot):
    if myglobals.CHANNELS:
        for channel in myglobals.CHANNELS:
            bot.send_message(channel, "Ya llegue putos...")