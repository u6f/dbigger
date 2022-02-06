import requests, os, random, string
from random import sample
from string import digits
from os import system
from requests import post, Session
o = open('links.txt', 'a')
system('clear')
print("""      _ _     _                       
     | | |   (_)                      
   __| | |__  _  __ _  __ _  ___ _ __ 
  / _` | '_ \| |/ _` |/ _` |/ _ \ '__|
 | (_| | |_) | | (_| | (_| |  __/ |   
  \__,_|_.__/|_|\__, |\__, |\___|_|   
                 __/ | __/ |          
   Made By u8f   |___/ |___/  Free Nudes
				Or IDs
""")
while True:
	id = "".join(sample(digits, 4))
	ses = Session()
	r = ses.get(f"https://imgdb.net/{id}")
	if "Not Found" not in r.text:
		o.write(f"\nhttps://imgdb.net/{id}")
		print(f"[\033[1;32;40m>\033[1;37;40m] https://imgdb.net/{id}")
