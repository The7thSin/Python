#Version 1.0 by George Dimitrov
#License The MIT License (MIT)
#Copyright 2019 George Dimitrov
#Work in progress

import digitalocean

mytoken="INSER YOUR API KEY"

manager = digitalocean.Manager(token=mytoken)

print("Pick Server Name")

server_name = input("Server Name: ")

print("Pick ssh keys to use")
print(manager.get_all_sshkeys())

input_keys = input("SSH Key IDs: ").split(",")

#picked_keys = []
#for key in input_keys:
#    picked_keys.append(key)

my_keys = []
for ssh_key in input_keys:
    the_key = manager.get_ssh_key(ssh_key)
    my_keys.append(the_key)


droplet = digitalocean.Droplet(token=mytoken,
                               name=server_name,
                               region='ams3',
                               image='ubuntu-18-04-x64',
                               size='s-2vcpu-2gb',
                               ssh_keys=my_keys)
droplet.create()


def server_status():
    actions = droplet.get_actions()
    for action in actions:
        action.load()
        # Once it shows complete, droplet is up and running
        return action.status


print("Creating Server")

while server_status() == "in-progress":
    server_status()

print("Server Created")
