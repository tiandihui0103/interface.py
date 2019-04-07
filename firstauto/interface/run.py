import config,json,unittest,HTMLTestRunner,sys
from helper import request,unit
from helper.api_v1 import api,http
from testcase.api_v1 import login
conf = config.Conf
testunit = unittest.TestSuite();
testunit.addTest(unittest.makeSuite(login.Loginin))
fw = open('C:/Python35/Webx_Report/sincaitestreport_.html', 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fw, title='获取前一条用例执行结果')
runner.run(testunit)
