#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import hiredis


class Parser(object):

    def __init__(self):
        self.reader = hiredis.Reader()
        self.reader.setmaxbuf(0)

    def parse_command(self, request):
        self.reader.feed(request)
        try:
            command = self.reader.gets()
            if command is not False:
                return command
        except hiredis.ProtocolError:
            return False
        return False
