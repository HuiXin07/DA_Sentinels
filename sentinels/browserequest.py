import requests
url = 'http://192.168.206.180/zipper'
r = requests.get(url)
print(r.text)

print("Status code:")
print("\t *", r.status_code)

h = requests.head(url)
print("Header")
print("**********")
for i in h.headers:
     print("\t",i,":", h.headers[i])
print("**********")
headers = {
 'User-Agent': 'Mobile'
}

url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)