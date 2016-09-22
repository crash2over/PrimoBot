# -*- coding: utf-8 -*-
import random

from utils import myglobals


def mywhores(mytext):
    if "-random-" in mytext:
        index = int(random.random() * 1000.0) % (len(myglobals.PUTAS))
        puta = myglobals.PUTAS[index]

        index = int(random.random() * 1000.0) % (len(myglobals.PUTASPHRASES))
        putaphrase = myglobals.PUTASPHRASES[index]
        if '@crassh' in puta:
            return (puta + "ese si me hace mujer y monta rico verdad @daronwolff")
        else:
            return (puta + putaphrase)
    else:
        return "Que quieres?"