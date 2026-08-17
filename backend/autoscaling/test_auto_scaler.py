import sys

sys.path.append("../simulation")

from virtual_server import VirtualServer
from auto_scaler import AutoScaler


# Create 3 servers
server1 = VirtualServer(1)
server2 = VirtualServer(2)
server3 = VirtualServer(3)

servers = [server1, server2, server3]


# Create AutoScaler
auto_scaler = AutoScaler(servers)


# Add 450 users to Server 1
server1.add_users(450)


# Show server status
print("Before scaling:")
for server in servers:
    print(server.get_status())


# Check if scaling is needed
auto_scaler.check_scaling()


# Show servers after scaling
print("\nAfter scaling:")
for server in servers:
    print(server.get_status())