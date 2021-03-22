import redis


class BusContext:
    def __init__(self, host, port, address):
        self.host = host
        self.port = port
        self.address = address
        self.conn = redis.Redis(host=host, port=port)

    @property
    def Host(self):
        return self.host

    @property
    def Port(self):
        return self.port

    @property
    def Address(self):
        return self.address

    @property
    def Connection(self):
        return  self.conn
