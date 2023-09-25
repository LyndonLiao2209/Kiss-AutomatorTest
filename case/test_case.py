import os
import sys
from util.smartPath import smart
# sys.path.append("E:/Teacher/Imooc/AppiumPython")
import unittest
# import HTMLTestRunner
import pytest_html
import threading
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from business.login_business import LoginBusiness
print(os.getcwd())
smart = smart()
smart.smartPath()
class ParameTestCase(unittest.TestCase):
	def __init__(self,methodName='runTest',param=None):
		super(ParameTestCase,self).__init__(methodName)
		self.param = param
		global params
		params = param

class CaseTest(ParameTestCase):
	@classmethod
	def setUpClass(cls):   #测试套件初始化
		global params
		print( "这个是setupclass里面的参数:",params)
		if params == 0:
			port = 4723
			device = 'R9PRB0EY45W'
		else:
			port = 4700
			device = 'R9PRB0EY45W'
			capabilities = {
				"platformName": "Android",
				"automationName":"UiAutomator2",
				"deviceName": "R9PRB0EY45W",
				"app": "D:\\package\\Kiss_debug_1.4.12_0904_1841.apk",
				"appActivity": "com.stardust.kissreader.SplashActivity",
				"appPackage": "com.stardust.kissreader",
				# "appWaitActivity":"cn.com.open.mooc.user.register.MCPhoneRegisterAty",
				"noReset": "true"
			}
		cls.driver = webdriver.Remote("http://127.0.0.1:"+str(port)+"/wd/hub",capabilities)
		time.sleep(10)
		cls.login_business = LoginBusiness(cls.driver)

	def setUp(self):  #测试用例初始化
		print( "this is setup")

	def test_01(self):
		print( "这个是测试方法里面的：",self.param)
		# time.sleep(3)
		# self.login_business.login_pass()
		#self.assertNotEqual(1,2)
		#self.assertTrue(flag)
		#self.assertFalse(flag)
	#@unittest.skip("CaseTest")
	def test_02(self):
		print( "this is case02")
		# flag = self.login_business.login_user_error()
		# self.assertTrue(flag)
	def tearDown(self):
		print( "this is teardown")
	@classmethod
	def tearDownClass(cls):
		print( "this is class teardown")
#
# def get_suite(i):
# 	suite = unittest.TestSuite()
# 	print("parame is:"+str(i))
# 	suite.addTest(CaseTest("test_02",param=i))
# 	suite.addTest(CaseTest("test_01",param=i))
# 	unittest.TextTestRunner().run(suite)   #运行测试套件的方法
# 	#html_file = "E:/Teacher/Imooc/AppiumPython/report/report"+str(i)+".html"
# 	#fp = file(html_file,"wb")
# 	#HTMLTestRunner.HTMLTestRunner(stream=fp).run(suite)

if __name__ == '__main__':
	pass
	# get_suite(0)
	# threads = []
	# for i in range(2):
	# 	print( i)
	# 	t = threading.Thread(target=get_suite,args=(i,))
	# 	threads.append(t)
	# for j in threads:
	# 	j.start()
