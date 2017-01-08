#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import pygtail


class Tailer():

    def __init__(self, logfile, offset_file):
        self.logfile = logfile
        self.offset_file = offset_file

    def ireadlines(self):
        tailer = pygtail.Pygtail(self.logfile, offset_file=self.offset_file)
        for line in tailer:
            yield line
