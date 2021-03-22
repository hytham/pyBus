from datetime import time
from unittest import TestCase

from Bus.BusContext import BusContext
from Bus.Busutil import busutil


class Testbusutil(TestCase):

    def test_send(self):
        ctx = BusContext("10.0.0.66", 6379, "test")
        bus = busutil(ctx)

        bus.Send("this is a test",time.time())
        msg,isnew = bus.Read()

        self.assertTrue(msg == "this is a test")

    def test_read(self):
        self.fail()
