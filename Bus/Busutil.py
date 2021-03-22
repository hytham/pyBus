from abc import ABC, abstractmethod
from datetime import time
import hashlib


class busutil(ABC):
    def __init__(self, buscontext):
        self.buscontext = buscontext
        self.oldmessage_timestamp = None

    def Send(self, msg):
        """ Send a message ge to redis"""
        ts = hashlib.sha256("this is a test".encode()).hexdigest()
        payload = {
            "msg":msg,
            "ts": ts
        }

        self.buscontext.Connection.hmset(self.buscontext.Address,payload)

        self.oldmessage_timestamp = ts

    def Read(self):
        """ Read a message and compair it with last message time stamp """
        payload = self.buscontext.Connection.hgetall(self.buscontext.Address)
        msg = payload[b"msg"]
        timestamp = payload[b"ts"]
        isNew = self.oldmessage_timestamp != timestamp
        return (msg, isNew)

    def Run(self):
        """
            Run throw an infinite loop that will read its current message execute it
            The implementation class must call send if it need to pass it to an other unit
        """
        while True:
            data, isnew = self.Read()
            if (isnew):
                data = self.Execute(data,time.time())
