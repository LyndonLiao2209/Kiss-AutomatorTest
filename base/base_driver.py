import json
import sys
import os
import time
import random
from appium import webdriver
from util.write_user_command import WriteUserCommand
fatherPath = os.path.abspath(os.path.join(os.getcwd(),".."))
sys.path.append(fatherPath)
class BaseDriver:
	sysPort = random.randint(10000,60000)
	print("sysPort is:",sysPort)
	def android_driver(self,i):
		print("this is android_driver:",i)
		#devices_name adb devices
		write_file = WriteUserCommand()
		devices = write_file.get_value('user_info_'+str(i),'deviceName')
		print("devices is:"+str(devices))
		port = write_file.get_value('user_info_'+str(i),'port')
		print("port is："+port)
		capabilities = {
		  "platformName": "Android",
		  "automationName":"UiAutomator2",   #指定UiAutomator2
		  "deviceName": devices,  #仅设备类型
		  "udid": devices,   #区分设备
		  "app": r"D:\package\Kiss_release_1.4.12_0904_1842.apk",
		  "appActivity": "com.stardust.kissreader.SplashActivity",
		  "appPackage": "com.stardust.kissreader",
		  # "appWaitActivity":"cn.com.open.mooc.user.login.MCLoginActivity",
		  "noReset":"true",
		  # "platforVersion":"13",   #版本号一定要对，要么就不填写。
		  "newCommandTimeout":'180',
		  "uiautomator2ServerLaunchTimeout":'20000',  # 设置为 60000 毫秒（60 秒）
		  "systemPort": self.sysPort,
		}
		print("capabilities is:", capabilities)
		driver = webdriver.Remote("http://127.0.0.1:"+port+"/wd/hub",capabilities)
		# 设置缺省等待时间
		driver.implicitly_wait(20)
		# time.sleep(10)
		return driver



if __name__ == '__main__':
	BaseDriver = BaseDriver()
	BaseDriver.android_driver(1)


