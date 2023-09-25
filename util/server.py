import sys
# sys.path.append("..")
from util.dos_cmd import DosCmd
from util.port import Port
import threading
import multiprocessing
import time
from util.write_user_command import WriteUserCommand
# import sys
# sys.path.append('')
class Server:

	def __init__(self):
		self.dos = DosCmd()
		self.device_list = self.get_devices()
		self.write_file = WriteUserCommand()
	def get_devices(self):
		'''
		获取设备信息
		'''
		
		devices_list = []
		result_list = self.dos.excute_cmd_result('adb devices')
		if len(result_list)>=2:
			for i in result_list:
				if 'List' in i:
					continue
				devices_info = i.split('\t')
				if devices_info[1] == 'device':
					devices_list.append(devices_info[0])
			return devices_list
		else:
			return None
	def create_port_list(self,start_port):
		'''
		创建可用端口
		'''
		port = Port()
		port_list = []
		port_list = port.create_port_list(start_port,self.device_list)
		return port_list

	def create_command_list(self,i):
		'''
		生成命令
		'''
		#appium -p 4700 -bp 4701 -U 127.0.0.1:21503
		
		command_list = []
		appium_port_list = self.create_port_list(4700)
		bootstrap_port_list = self.create_port_list(4900)
		device_list = self.device_list
		command = "start /b appium --command-timeout 60000 -p "+str(appium_port_list[i])+" -bp "+str(bootstrap_port_list[i])+" -U "+device_list[i]+" --no-reset --session-override --log log/test88.log"
		#appium -p 4723 -bp 4726 -U 127.0.0.1:62001 --no-reset --session-override --log E:/Teacher/Imooc/AppiumPython/log/test01.log
		command_list.append(command)
		print("生成的命令列表：",command_list)
		# print("adb:"+str(command_list))
		self.write_file.write_data(i,device_list[i],str(bootstrap_port_list[i]),str(appium_port_list[i]))   #写入设备信息到yaml中

		return command_list

	def start_server(self,i):
		'''
		启动服务
		'''
		print("start_server:",i)
		self.start_list = self.create_command_list(i)
		print("启动appium server列表：",self.start_list[0])
		print("start_server:", i)

		self.dos.excute_cmd(self.start_list[0])

	def kill_server(self):
		server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
		if len(server_list)>0:
			self.dos.excute_cmd('taskkill -F -PID node.exe')

	def main(self):  #主程序，启动所有设备对应的appium server并启动多线程跑
		thread_list = []
		self.kill_server()
		# time.sleep(3)
		self.write_file.clear_data()
		print("server中的设别列表：",self.device_list)
		for i in range(len(self.device_list)):
			appium_start = multiprocessing.Process(target=self.start_server,args=(i,)) #启动所有设备对应的appium server
			thread_list.append(appium_start)
		for j in thread_list:
			j.start()
		time.sleep(20)


if __name__ == '__main__':
	server = Server()
	# server.kill_server()
	# server.start_server(0)
	server.main()
