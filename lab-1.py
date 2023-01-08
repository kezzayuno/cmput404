import os 
import requests 

# Shows version of requests library
os.system('cmd /c "pip show requests"')

# curl 
google = requests.get('https://www.google.com/').text
print(google)

# curl download itself / prints itself 
dir = os.getcwd()
lab_1_github = requests.get('https://raw.githubusercontent.com/kezzayuno/cmput404/master/lab-1.py?token=GHSAT0AAAAAAB444ROX7BWI5LENZYKVMIGSY53KLJQ')

# Saves Python script from GitHub into local directory 
lab_1_local = open(dir + 'from_github.py', 'wb')
lab_1_local.write(lab_1_github.content)
lab_1_local.close()

# Display source code from GitHub
print(lab_1_github.content)

