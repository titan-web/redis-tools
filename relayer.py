#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

from kafka import KafkaProducer


class Relayer(object):

    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers='localhost:1234')
        self.topic = "topic"

    def send_msg(self, value):
        self.producer.send(self.topic, value)
