# -*- coding: utf-8 -*-

from utils import myglobals
from utils import filemanager


def loadChannels():
    myfile = filemanager.MyFile('channels', True, False, False)
    myglobals.CHANNELS = myfile.read_lines()


def Check2Save(channel):
    if myglobals.CHANNELS:
        if (str(channel) + '\n') not in myglobals.CHANNELS:
            print (str(channel) + '\n')
            print myglobals.CHANNELS
            saveChannel(channel, False, True)
    else:
        saveChannel(channel, True, False)


def saveChannel(channel, write, append):
    myfile = filemanager.MyFile('channels', False, write, append)
    myfile.write_line(str(channel) + "\n")
    loadChannels()


def sayHello2Channels(bot):
    if myglobals.CHANNELS:
        for channel in myglobals.CHANNELS:
            msg = "Ya llegue bitches... El colega es mi putito"
            msg += "\nChequen https://github.com/crash2over/PrimoBot"
            bot.send_message(channel, msg)