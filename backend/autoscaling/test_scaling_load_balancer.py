import sys

sys.path.append("../simulation")
sys.path.append("../load_balancer")

from virtual_server import VirtualServer
from auto_scaler import AutoScaler
from round_robin import RoundRobin


# Create servers
server1 = VirtualServer(1)
server2 = VirtualServer(2)
server3 = VirtualServer(3)

servers = [server1, server2, server3]


# Create components using the SAME server list
load_balancer = RoundRobin(servers)
auto_scaler = AutoScaler(servers)


# Overload Server 1
server1.add_users(450)

print("Before scaling:")
for server in servers:
    print(server.get_status())


# Check scaling
auto_scaler.check_scaling()

print("\nAfter scaling:")
for server in servers:
    print(server.get_status())


# Test Round Robin after scaling
print("\nRound Robin after scaling:")

for i in range(8):

    server = load_balancer.get_next_server()

    print(
        "Request", i + 1,
        "→ Server", server.server_id
    )