import unittest,sys,json,HTMLTestRunner
sys.path.append("../..")
from helper import request,unit
from helper.api_v1 import api,http
from parameterized import parameterized

class Loginin(unittest.TestCase):
	@parameterized.expand(unit.makeCsvData("./data/api_v1/logintest.csv"))
	def test_getHttpBody(self,username,password,loginpass,nonce):
		bodyData = {"username":username,"password":password,"loginpass":loginpass,"nonce":nonce}
		data = json.dumps(bodyData).encode(encoding='utf-8')
		url = api.getkey()
		headers = http.getHttpHeader()
		loginresult = request.sendPost(url,data,headers)
		jsonresult = json.loads(loginresult.decode('utf-8'))
		self.assertEqual(jsonresult['status'],10000)
#		print(jsonresult['status'])


#		print(loginresult)


if __name__ == '__main__':
   unittest.main()
'''
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Loginin))
    fw = open('C:/Python35/Webx_Report/sincaitestreport_.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fw, title='获取前一条用例执行结果')
    runner.run(suite)
'''

'''
class TestAdd(unittest.TestCase):
	def test_getHttpBody(self):
		data = {"username":"huashan","password":"123qwe","loginpass":"123qwe","nonce":"e65965849709bda2a8c2f62a6e4ec444"}
		data = json.dumps(data).encode(encoding='utf-8')
		url = api.getkey()
		headers = http.getHttpHeader()
		result = request.sendPost(url,data,headers)
		print(result)

if __name__ == '__main__':
    unittest.main()

'''

'''
#原始能执行成功
def wotama():
	data = {"username":"huashan","password":"123qwe","loginpass":"123qwe","nonce":"e65965849709bda2a8c2f62a6e4ec969"}
	data = json.dumps(data).encode(encoding='utf-8')
	url = api.getkey()
	headers = http.getHttpHeader()
	result = request.sendPost(url,data,headers)
	print(result)
wotama()
'''


