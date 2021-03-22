from datetime import time
from unittest import TestCase

from Bus.BusContext import BusContext
from Bus.npBusutil import npbusutil

import hashlib

class Testnpbusutil(TestCase):


    def test_send_then_read_test(self):
        ctx = BusContext("10.0.0.200", 6379, "test")
        bus = npbusutil(ctx)

        bus.Send("this is a test")
        msg, isnew = bus.Read()

        self.assertTrue(msg == "this is a test")


