# -*- coding: utf-8 -*-


class MyFile:

    def __init__(self, name, read, write, appending):
        try:
            if read and write:
                self.file = open(name, 'r+')
            elif read:
                self.file = open(name, 'r')
            elif write:
                self.file = open(name, 'w')
            elif appending:
                self.file = open(name, 'a')
        except:
            self.file = None
            print ("Error opening file...")

    def read_lines(self):
        if self.file:
            mylist = self.file.readlines()
            self.file.close()
        else:
            print ("On read_line no file opened")
            mylist = None
        return mylist

    def write_line(self, data):
        if self.file:
            self.file.write(data)
            self.file.close()
            return True
        else:
            print ("On write_line no file opened")
            return False

    def write_all(self, phrases):
        if self.file:
            for phrase in phrases:
                self.file.write(phrase)
            self.file.close()
            return True
        else:
            print ("On write_all no file opened")
            return False
