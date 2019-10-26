# Version 1.0 by George Dimitrov
# License The MIT License (MIT)
# Copyright 2019 George Dimitrov
# Work in progress

import digitalocean

# Digital Ocean  API Token
my_token = "Your Token Here"

# Region
region = "nyc3"

# Image
dist = "ubuntu-18-04-x64"

# Droplet Size
size = "s-1vcpu-1gb"

manager = digitalocean.Manager(token=my_token)

print("Pick Server Name")

server_name = "Test"  # input("Server Name: ")

print("Pick ssh keys to use")
print(manager.get_all_sshkeys())

input_keys = input("SSH Key IDs: ").split(",")

# picked_keys = []
#   for key in input_keys:
#       picked_keys.append(key)

my_keys = []
for ssh_key in input_keys:
    the_key = manager.get_ssh_key(ssh_key)
    my_keys.append(the_key)

# Droplet Creating
droplet = digitalocean.Droplet(token=my_token, name=server_name, region=region, image=dist, size=size, ssh_keys=my_keys)
droplet.create()

# Server Status Check
def server_status():
    actions = droplet.get_actions()
    for action in actions:
        action.load()
        # Once it shows complete, droplet is up and running
        return action.status


print("Creating Server")

# Wait for Server Created
while server_status() == "in-progress":
    server_status()

print("Server Created")
