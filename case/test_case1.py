import os
fatherPath = os.path.abspath(os.path.join(os.getcwd(),))
import sys
sys.path.append(fatherPath)
import unittest
# import HTMLTestRunner
import threading
import multiprocessing
from util.server import Server
import time
from appium import webdriver
from business.login_business import LoginBusiness
from util.write_user_command import WriteUserCommand

class ParameTestCase(unittest.TestCase):
	def __init__(self,methodName='runTest'):
		super(ParameTestCase,self).__init__(methodName)
		ParameTestCase.parame = parame
		print("重写的parame：",ParameTestCase.parame)

class CaseTest(ParameTestCase):
	@classmethod
	def setUpClass(cls):
		print( "setUpclass---->",ParameTestCase.parame)
		# cls.login_business = LoginBusiness(parames)

	def setUp(self):
		print( "this is setup\n")


	def test_01(self):
		print( "test case 里面的参数",ParameTestCase.parame)
		# self.login_business.login_pass()


		#self.assertNotEqual(1,2)
		#self.assertTrue(flag)
		#self.assertFalse(flag)
	#@unittest.skip("CaseTest")
	def test_02(self):
		# self.login_business.login_user_error()
		print( "this is case02\n")
		self.assertTrue(True)
	def tearDown(self):
		time.sleep(1)
		print( "this is teardown\n")
		# if sys.exc_info()[0]:
			# self.login_business.login_handle.login_page.driver.save_screenshot("jpg/test02.png")


	@classmethod
	def tearDownClass(cls):
		time.sleep(1)
		print( "this is class teardown\n")
		#cls.driver.quit()

def appium_init():
	server = Server()
	server.main()

def get_suite(i):
	print( "get_suite里面的",i)
	suite = unittest.TestSuite()
	suite.addTest(CaseTest("test_02",parame=i))
	suite.addTest(CaseTest("test_01",parame=i))
	
	#unittest.TextTestRunner().run(suite)
	html_file = "report/report"+str(i)+".html"
	fp = html_file(html_file,"wb")
	# HTMLTestRunner.HTMLTestRunner(stream=fp).run(suite)
def get_count():
	write_user_file = WriteUserCommand()
	count = write_user_file.get_file_lines()
	return count

if __name__ == '__main__':
	pass
	# appium_init()
	# get_suite(1)
	# threads = []
	# for i in range(get_count()):
	# 	print( i)
	# 	t = multiprocessing.Process(target=get_suite,args=(i,))
	# 	threads.append(t)
	# for j in threads:
	# 	j.start()

		#time.sleep(1)
	#time.sleep(80)
