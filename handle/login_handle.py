#coding=utf-8
from page.login_page import LoginPage
class LoginHandle:
	def __init__(self,i):
		self.login_page = LoginPage(i)
	#操作登录页面的元素
	def click_facebook_login(self):
		'''
		进入到登录界面并点击登录按钮
		'''
		self.login_page.get_facebook_login_element().click()

	def click_google_login(self):
		'''
		点击google登录
		'''
		self.login_page.get_google_login_element().click()




	#
	# def send_username(self,user):
	# 	'''
	# 	输入用户名
	# 	'''
	# 	self.login_page.get_username_element().send_keys(user)
	#
	# def send_password(self,password):
	# 	'''
	# 	输入密码
	# 	'''
	# 	self.login_page.get_password_element().send_keys(password)
	#
	# def click_login(self,loginMethod="facebookLogin"):
	# 	'''
	# 	进入到登录界面并点击登录按钮
	# 	'''
	# 	if
	# 	self.login_page.getLoginElement(loginMethod).click()
	# 	# elif loginMethod == "googleLogin":
	# 	# 	self.login_page.getLoginElement(loginMethod).click()
	# 	# self.login_page.get_login_button_element().click()
	#
	# def click_forget_password(self):
	# 	'''
	# 	点击忘记密码
	# 	'''
	# 	self.login_page.get_forget_password_element().click()
	#
	# def click_register(self):
	# 	'''
	# 	点击注册按钮
	# 	'''
	# 	self.login_page.get_register_element()
	#
	# def get_fail_tost(self,message):
	# 	'''
	# 	获取tost，根据返回信息进行反数据
	# 	'''
	# 	tost_element = self.login_page.get_tost_element(message)
	# 	if tost_element:
	# 		return True
	# 	else:
	# 		return False
		