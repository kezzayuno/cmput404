import os 
import requests 

# Shows version of requests library
os.system('cmd /c "pip show requests"')

# curl 
google = requests.get('https://www.google.com/')
print(google)

# curl download itself / prints itself 
lab_1 = requests.get('https://raw.githubusercontent.com/kezzayuno/cmput404/master/lab-1.py?token=GHSAT0AAAAAAB444ROW5ADJLW4NAHIIHW42Y53JVAA')
print(lab_1)

