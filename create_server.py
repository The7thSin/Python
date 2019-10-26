# Version 1.0 by George Dimitrov
# License The MIT License (MIT)
# Copyright 2019 George Dimitrov
# Work in progress

import digitalocean
import os

# USER CONFIG
# Digital Ocean  API Token
my_token = open('api_key.txt', 'r').readline().rstrip('\n')

# Region
region = "nyc3"

# Image
dist = "centos-7-x64"

# Droplet Size
size = "s-1vcpu-1gb"

# SCRIPT START


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


clear_screen()

manager = digitalocean.Manager(token=my_token)

print("Pick Server Name")

server_name = input("Server Name: ")

# Droplet Tag
my_tag = [server_name]

print("Pick ssh keys to use")
print(manager.get_all_sshkeys())

input_keys = input("SSH Key IDs: ").split(",")

my_keys = []
for ssh_key in input_keys:
    the_key = manager.get_ssh_key(ssh_key)
    my_keys.append(the_key)

# Droplet Creating
droplet = digitalocean.Droplet(token=my_token, name=server_name, region=region, image=dist, size=size, ssh_keys=my_keys, tags=my_tag)
droplet.create()

# Server Status Check


def server_status():
    actions = droplet.get_actions()
    for action in actions:
        action.load()
        # Once it shows complete, droplet is up and running
        return action.status

# Get Server IP address

def get_droplet_ip():
    cur_droplets = manager.get_all_droplets()
    # Iterate through all existing droplets
    for i in cur_droplets:
        if i.name == server_name:
            return i.ip_address

print("Creating Server")

# Wait for Server Created
while server_status() == "in-progress":
    server_status()

print("Your Droplet IP is {}".format(get_droplet_ip()))
print("Server Created, Bye Bye!")
