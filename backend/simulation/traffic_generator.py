import random


class TrafficGenerator:

    def __init__(self, min_users=100, max_users=5000):
        self.min_users = min_users
        self.max_users = max_users

    def generate_users(self):
        return random.randint(self.min_users, self.max_users)