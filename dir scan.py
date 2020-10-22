import requests
import sys

url = sys.argv[1] //url参数
dir = sys.argv[2] //字典参数
with open("dir","r") as f:
    for line in f.readlines():
        line = line.strip()
        r = requests.get(url+line)
        if r.status_code == 200:
            print("url:"+r.url+"exist")
