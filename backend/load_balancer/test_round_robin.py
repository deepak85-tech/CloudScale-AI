from round_robin import RoundRobin


servers = ["Server 1", "Server 2", "Server 3"]

load_balancer = RoundRobin(servers)

for i in range(10):
    server = load_balancer.get_next_server()
    print(f"Request {i + 1} → {server}")