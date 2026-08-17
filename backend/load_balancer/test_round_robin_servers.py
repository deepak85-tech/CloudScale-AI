from round_robin import RoundRobin
import sys

sys.path.append("../simulation")

from virtual_server import VirtualServer


server1 = VirtualServer(1)
server2 = VirtualServer(2)
server3 = VirtualServer(3)

servers = [server1, server2, server3]

load_balancer = RoundRobin(servers)

for i in range(10):

    server = load_balancer.get_next_server()

    server.add_users(50)

    status = server.get_status()

    print(
        "Request", i + 1,
        "→ Server", status["server_id"],
        "| Users:", status["users"],
        "| CPU:", status["cpu"], "%",
        "| Memory:", status["memory"], "%",
        "| Latency:", status["latency"],
        "| Status:", status["status"]
    )