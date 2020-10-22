import requests
import sys

url = sys.argv[1]
dir = sys.argv[2]
with open("dir","r") as f:
    for line in f.readlines():
        line = line.strip()
        r = requests.get(url+line)
        if r.status_code == 200:
            print("url:"+r.url+"exist")