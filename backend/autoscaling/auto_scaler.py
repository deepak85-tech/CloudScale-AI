import sys

sys.path.append("../simulation")

from virtual_server import VirtualServer


class AutoScaler:

    def __init__(self, servers):
        self.servers = servers
        self.next_server_id = len(servers) + 1

    def check_scaling(self):

        for server in self.servers:

            if server.cpu_usage >= 90:
                self.scale_out()
                return True

        return False

    def scale_out(self):

        new_server = VirtualServer(self.next_server_id)

        self.servers.append(new_server)

        self.next_server_id += 1

        print("New server added:", new_server.server_id)