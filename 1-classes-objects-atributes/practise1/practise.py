class Server:
    counter = 1

    def __init__(self):
        self.buffer = []
        self.IP = self.counter
        Server.counter += 1
        self.router = None

    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        copy_data = list(self.buffer)
        self.buffer.clear()
        return copy_data

    def get_ip(self):
        return self.IP


class Router:
    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server):
        self.servers[server.get_ip()] = server
        server.router = self

    def unlink(self, server):
        unlinked_server = self.servers.pop(server.get_ip(), False)
        if unlinked_server:
            unlinked_server.router = None

    def send_data(self):
        for data in self.buffer:
            if data.IP in self.servers:
                self.servers[data.IP].buffer.append(data)

        self.buffer.clear()


class Data:
    def __init__(self, data, IP):
        self.data = data
        self.IP = IP
