class VirtualServer:

    def __init__(self, server_id, max_users=500):

        self.server_id = server_id
        self.max_users = max_users

        self.current_users = 0
        self.cpu_usage = 0
        self.memory_usage = 0
        self.latency = 0
        self.status = "Healthy"
        self.cost = 5.0

    def add_users(self, users):

        self.current_users += users

        self.cpu_usage = (self.current_users / self.max_users) * 100

        self.memory_usage = (self.current_users / self.max_users) * 80

        self.latency = 10 + (self.cpu_usage * 0.2)

        if self.cpu_usage >= 90:
            self.status = "Overloaded"
        elif self.cpu_usage >= 70:
            self.status = "High Load"
        else:
            self.status = "Healthy"

    def get_status(self):

        return {
            "server_id": self.server_id,
            "users": self.current_users,
            "cpu": round(self.cpu_usage, 2),
            "memory": round(self.memory_usage, 2),
            "latency": round(self.latency, 2),
            "status": self.status,
            "cost": self.cost
        }