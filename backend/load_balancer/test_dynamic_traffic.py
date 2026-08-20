import sys

sys.path.append("../simulation")
sys.path.append("../autoscaling")

from virtual_server import VirtualServer
from traffic_generator import TrafficGenerator
from round_robin import RoundRobin
from auto_scaler import AutoScaler


# -------------------------
# Create servers
# -------------------------

server1 = VirtualServer(1)
server2 = VirtualServer(2)
server3 = VirtualServer(3)

servers = [server1, server2, server3]


# -------------------------
# Create traffic generator
# -------------------------

traffic = TrafficGenerator(min_users=1350, max_users=1350)


# -------------------------
# Create load balancer
# -------------------------

load_balancer = RoundRobin(servers)


# -------------------------
# Create auto scaler
# -------------------------

auto_scaler = AutoScaler(servers)


# -------------------------
# Generate traffic
# -------------------------

users = traffic.generate_users()

print("Generated users:", users)


# -------------------------
# Send traffic
# -------------------------

for i in range(users):

    server = load_balancer.get_next_server()

    server.add_users(1)


# -------------------------
# Before scaling
# -------------------------

print("\nBefore scaling:")

for server in servers:
    print(server.get_status())


# -------------------------
# Check scaling
# -------------------------

auto_scaler.check_scaling()


# -------------------------
# After scaling
# -------------------------

print("\nAfter scaling:")

for server in servers:
    print(server.get_status())


# -------------------------
# New traffic after scaling
# -------------------------

print("\nNew traffic after scaling:")

for i in range(8):

    server = load_balancer.get_next_server()

    print(
        "Request",
        i + 1,
        "→ Server",
        server.server_id
    )