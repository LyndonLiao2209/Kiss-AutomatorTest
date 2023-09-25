#Bottom不属于任何页面，没有page和business
from base.base_driver import BaseDriver
class bottomHandle:
	def __init__(self,i):
		self.driver = BaseDriver(i)
	#操作登录页面的元素
	def click_login(self,loginMethod):
		'''
		进入到登录界面并点击登录按钮
		'''
		if loginMethod == "facebookLogin":
			self.login_page.get_facebook_login_element().click()
		elif loginMethod == "googleLogin":
			self.login_page.get_google_login_element().click()
		elif loginMethod == "emailLogin":
			self.login_page.get_email_login_element().click()
		else:
			self.login

	def click_google_login(self):
		'''
		点击google登录
		'''
		self.login_page.get_google_login_element().click()


if __name__ =="__main__":
	pass