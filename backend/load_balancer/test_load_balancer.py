from round_robin import RoundRobin
import sys

sys.path.append("../simulation")

from virtual_server import VirtualServer
from traffic_generator import TrafficGenerator


# Create servers
server1 = VirtualServer(1)
server2 = VirtualServer(2)
server3 = VirtualServer(3)

servers = [server1, server2, server3]


# Create Round Robin load balancer
load_balancer = RoundRobin(servers)


# Create traffic generator
traffic = TrafficGenerator(100, 500)


# Generate traffic
users = traffic.generate_users()

print("Generated users:", users)


# Distribute users using Round Robin
for i in range(users):

    server = load_balancer.get_next_server()

    server.add_users(1)


# Show final server status
for server in servers:
    print(server.get_status())