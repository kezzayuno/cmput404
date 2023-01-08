import os 
import requests 

# Shows version of requests library
os.system('cmd /c "pip show requests"')

# curl 
google = requests.get('https://www.google.com/')
print(google)

