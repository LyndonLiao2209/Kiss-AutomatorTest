import sys
import os
fatherPath = os.path.abspath(os.path.join(os.getcwd(),".."))
sys.path.append(fatherPath)
import threading
import multiprocessing
from time import sleep
from util.server import  Server
# from KeyWord.get_data import GetData
# from KeyWord.action_method import ActionMethod
from util.server import Server
from util.write_user_command import  WriteUserCommand
from base.base_driver import BaseDriver
from KeyWord.get_data import GetData
from KeyWord.action_method import ActionMethod
from business.guideBusiness import  guideBusiness


class RunMain:
	# deviceList = None
	server = Server()

	def run_server(self,*args):
		self.server.main()   #启动所有appium server
		# self.deviceList = self.server.get_devices()   #引用类变量
		# RunMain.deviceList = self.server.get_devices()   #通过类引用类变量
		# print(RunMain.deviceList)
		# print("设备列表：",self.deviceList)
	#
	# def run_get_data(self,*args):  #启动所有driver
	# 	self.get_data = GetData()
	# 	self.get_data.get_data(args[0])
	#
	# def run_action_method(self,*args):
	# 	self.action_method = ActionMethod()
	# 	self.action_method.on_click(args[0])
	def run_driver(self,*args):  #启动所有driver
		self.driver = BaseDriver()
		print("driver多进程传的args: ",args)
		self.driver.android_driver(args[0])

	def run_guide(self,*args):

		self.guideBusiness = guideBusiness(args[0])
		print("driver多进程传的args: ",args)
		self.guideBusiness.lookBook()
		# self.driver.android_driver(args[0])


	def multiThreading(self):  #主程序，启动所有设备driver，并启动多线程跑
		thread_list = []
		readFile = WriteUserCommand()
		deviceList = readFile.read_data()  #读取yaml
		print("yaml读取的deviceList :",deviceList)
		# self.deviceList =
		# RunMain.deviceList = self.server.get_devices()  # 通过类引用类变量
		# readFile.get_value()
		# self.server.kill_server()
		# self.server.start_server()
		# self.write_file.clear_data()

		# self.deviceList = self.server.get_devices()
		for i in range(len(deviceList)):
			print("第一台设备",i)
			driver_start = multiprocessing.Process(target=self.run_driver,args=(i,)) #启动所有设备的driver
			thread_list.append(driver_start)
		for j in thread_list:
			j.start()
		sleep(15)


	def multiGuide(self):  #主程序，启动所有设备driver，并启动多线程跑
		thread_list = []
		readFile = WriteUserCommand()
		deviceList = readFile.read_data()  #读取yaml
		print("yaml读取的deviceList :",deviceList)
		# self.deviceList =
		# RunMain.deviceList = self.server.get_devices()  # 通过类引用类变量
		# readFile.get_value()
		# self.server.kill_server()
		# self.server.start_server()
		# self.write_file.clear_data()

		# self.deviceList = self.server.get_devices()
		for i in range(len(deviceList)):
			print("第一台设备",i)
			driver_start = multiprocessing.Process(target=self.run_guide,args=(i,)) #启动所有设备的driver
			thread_list.append(driver_start)
		for j in thread_list:
			j.start()
		sleep(15)


if __name__ == '__main__':
	run = RunMain()

	run.run_server()
	# run.multiThreading()
	run.multiGuide()
	# sleep(10)
	# run.multiThreading()

	# guideBusiness = guideBusiness()
	# guideBusiness