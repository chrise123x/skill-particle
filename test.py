from keys import *
import requests

print ("------------------")
print (args)

r = requests.post('https://api.particle.io/v1/devices/%s/sprinkler?' % device_id, data={'args': args, 'access_token':access_token})
print (r[0])
