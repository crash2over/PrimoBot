# -*- coding: utf-8 -*-

from utils import myglobals
from utils import filemanager


def loadPutas():
    myfile = filemanager.MyFile('putas', True, False, False)
    myglobals.PUTAS = myfile.read_lines()


def loadPutasPhrases():
    myfile = filemanager.MyFile('putasphrases', True, False, False)
    myglobals.PUTASPHRASES = myfile.read_lines()


def addPutasAndUpdate(message):
    try:
        myfile = filemanager.MyFile('putas', False, False, True)
        mytext = message.text + '\n'
        if '@' in mytext:
            if '@crassh' not in mytext:
                myfile.write_line(mytext.split(' ', 1)[1])
                loadPutas()
            return True
        else:
            return False
    except:
        return False


def addPutasPhraseAndUpdate(message):
    try:
        myfile = filemanager.MyFile('putasphrases', False, False, True)
        mytext = message.text + '\n'
        myfile.write_line(mytext.split(' ', 1)[1])
        loadPutasPhrases()
        return True
    except:
        return False