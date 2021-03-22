import io

import numpy as np
from Bus.Busutil import busutil


class npbusutil(busutil):

    def _adapt_array(self,arr):
        """
        http://stackoverflow.com/a/31312102/190597 (SoulNibbler)
        """
        out = io.BytesIO()
        np.save(out, arr)
        out.seek(0)
        return out.read()

    def _convert_array(self,text):
        out = io.BytesIO(text)
        out.seek(0)
        return np.load(out)

    def __init__(self,ctx):
        super(npbusutil, self).__init__(ctx)

    def Send(self, np_array):
        msg = self._adapt_array(np_array)
        super(npbusutil, self).Send(msg)

    def Read(self):
        text,isnew = super(npbusutil, self).Read()
        data = self._convert_array(text)
        assert isinstance(isnew, object)
        return data,isnew