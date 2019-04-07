from urllib import parse,request
import json
def sendPost(url,data,headers):
	req = request.Request(url=url,data=data,headers=headers)
	res = request.urlopen(req)
	res = res.read()
	return res
'''
	print(res)
textmod = {"username":"huashan","password":"123qwe","loginpass":"123qwe","nonce":"e65965849709bda2a8c2f62a6e4ec947"}
textmod = json.dumps(textmod).encode(encoding='utf-8')
###放到http.py中
headers = {"Content-Type": "application/vnd.sc-api.v1.json"}
###放到api.py中
url = 'http://pre.123ssc.net/api/auth/login'
sendPost()
'''