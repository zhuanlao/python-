import requests
import sys

url = sys.argv[1] #url参数
dir = sys.argv[2] #字典参数
#打开字典拼接url
with open("dir","r") as f:
    for line in f.readlines():
        line = line.strip()
        #http get请求url
        r = requests.get(url+line)
        #判断状态码，输出存在目录
        if r.status_code == 200:
            print("url:"+r.url+"exist")
