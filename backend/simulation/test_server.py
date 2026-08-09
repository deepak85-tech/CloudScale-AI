from virtual_server import VirtualServer


server = VirtualServer(1)

server.add_users(250)

print(server.get_status())