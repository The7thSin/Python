# Version 1.0 by George Dimitrov
# License The MIT License (MIT)
# Copyright 2019 George Dimitrov
# Work in progress

import digitalocean

# Digital Ocean  API Token
my_token = "Your Token here"

# Load API Key up
manager = digitalocean.Manager(token=my_token)

#Request all Droplets with IDs
droplet_ids = manager.get_all_droplets()
print(droplet_ids)

# Ask user which one he wants to remove
picked_id = input("Droplet ID: ")

# Deletes the droplet
droplet = digitalocean.Droplet(name=picked_id)
droplet.destroy()
