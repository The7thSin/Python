# Version 1.0 by George Dimitrov
# License The MIT License (MIT)
# Copyright 2019 George Dimitrov
# Work in progress

import digitalocean
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


clear_screen()

# Digital Ocean  API Token
my_token = open('api_key.txt', 'r').readline().rstrip('\n')

# Load API Key up
manager = digitalocean.Manager(token=my_token)

# Request all Droplets with IDs
droplet_ids = manager.get_all_droplets()
print(droplet_ids)

# Ask user which one he wants to remove
picked_id = input("Droplet ID: ")


def get_droplet_name():
    # Iterate through all existing droplets
    for i in droplet_ids:
        if i.id == picked_id:
            return i.name


print("Waring this with delete droplet {}".format(get_droplet_name()))

while True:

    usr_consent = input("[Y/n]: ")

    if usr_consent.lower() == "y":
        # Deletes the droplet
        droplet = digitalocean.Droplet(token=my_token, id=picked_id)
        droplet.destroy()
        print("You killed {} Jim!".format(get_droplet_name()))
        break
    elif usr_consent.lower() == "n":
        print("No Droplets Die Today \\(O v O)/!")
        break
    else:
        print("Invalid input dude.")
    continue
