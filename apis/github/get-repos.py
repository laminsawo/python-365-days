import requests

token = "61ad8e65cfa0e3acd9a67baa8428094eb4af29b3"
r =  requests.get('https://api.github.com/user', auth=('laminsawo', 's45272081G'))
r.status_code

