# -*- coding: utf-8 -*-

import random
from utils import myglobals
from utils import filemanager


def loadPhrases():
    myfile = filemanager.MyFile('phrases', True, False, False)
    myglobals.PHRASES = myfile.read_lines()


def addPhraseAndUpdate(message):
    try:
        myfile = filemanager.MyFile('phrases', False, False, True)
        mytext = message.text + '\n'
        myfile.write_line(mytext.split(' ', 1)[1])
        myfile = filemanager.MyFile('phrases', True, False, False)
        myglobals.PHRASES = myfile.read_lines()
        return True
    except:
        return False


def delPhraseAndUpdate(message):
    try:
        linenum = int(message.text.split(' ', 1)[1]) - 1
        myglobals.PHRASES.pop(linenum)
        myfile = filemanager.MyFile('phrases', False, True, False)
        myfile.write_all(myglobals.PHRASES)
        myfile = filemanager.MyFile('phrases', True, False, False)
        myglobals.PHRASES = myfile.read_lines()
        return True
    except:
        return False


def getRandomAndPhrase():
    dic = {}
    print str(len(myglobals.PHRASES))
    dic['random'] = int(random.random() * 1000.0) % (len(myglobals.PHRASES))
    dic['phrase'] = myglobals.PHRASES[dic['random']]
    return dic