class RoundRobin:

    def __init__(self, servers):
        self.servers = servers
        self.current_index = 0

    def get_next_server(self):
        server = self.servers[self.current_index]

        self.current_index = (
            self.current_index + 1
        ) % len(self.servers)

        return server