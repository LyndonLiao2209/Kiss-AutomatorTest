#coding=utf-8
from util.read_init import ReadIni
from appium.webdriver.common.mobileby import MobileBy
from robot.api import logger
import traceback     #python异常处理和跟踪库
from time import sleep
import datetime
#封装定位方式，支持id,className,xpath.
class GetByLocal:
	def __init__(self,driver):
		self.driver = driver
	def get_element(self,key,section):  #如key=facebookLogin,读取ini文件，获取定位方式，如id>login_button，返回id为login_button的元素
		read_ini = ReadIni()
		local = read_ini.get_value(key,section)
		if local != None:
			by = local.split('>')[0]
			local_by = local.split('>')[1]
			print("by:{},local_by:{}".format(by,local_by))
			try:
				if by == 'id':
					return self.driver.find_element(MobileBy.ID,local_by)
				elif by == 'className':
					return self.driver.find_element(MobileBy.CLASS_NAME,local_by)
				else:
					return self.driver.find_element(MobileBy.XPATH,local_by)
			except:
				logger.info("{}".format(traceback.format_exc()))
				self.driver.save_screenshot("../Screen/error{}.png".format(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))  # 错误捕获
				sleep(3)
				raise Exception("{}".format(traceback.format_exc()))


			# except:
			# 	#self.driver.save_screenshot("../jpg/test02.png")
			# 	return None

		else:
			return "元素定位信息为空"

if __name__ == '__main__':
	pass
	# get_by = GetByLocal(driver)
	# print(get_by.get_element('facebookLogin'))
	# import datetime
	#
	# # 获取当前时间
	# current_time = datetime.datetime.now()
	# print(current_time)
	# # 格式化时间
	# formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
	#
	# print("当前时间：", formatted_time)