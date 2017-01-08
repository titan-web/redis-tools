#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

from tailer import Tailer
from parser import Parser
import yaml


def main():
    stream = file('config.yaml', 'r')
    config = yaml.load(stream)

    tailer = Tailer(config.get('tail').get('aof_path'), "offset_file")
    parser = Parser()
    request = ""
    for line in tailer.ireadlines():
        request += line
        command = parser.parse_command(line)
        if not command:
            continue
        request = ""
        print command

if __name__ == "__main__":
    main()
