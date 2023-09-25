import sys
import os
import configparser
currentPath = os.getcwd()


class ReadIni:
	def __init__(self,file_path=None):  # 初始化，传入文件路径
		if file_path == None:
			self.file_path = '..\config\LocalElement.ini'  #当前路径为util，需要找父节点
			# self.file_path = 'config\LocalElement.ini'
		else:
			self.file_path = file_path
		self.data = self.read_ini()  # 获取配置文件信息


	def read_ini(self): # 读取配置文件
		read_ini = configparser.ConfigParser()
		read_ini.read(self.file_path)
		# print(read_ini.read(self.file_path))
		return read_ini

	#通过key获取对应的value.key为字典名，如：login_element，section为XX.ini中[XX]部分
	def get_value(self,key,section=None):  #section为XX.ini中[XX]部分，key为字典名，如：facebookLogin。
		if section == None:   #默认传登录元素
			section = 'login_element'
		try:
			value = self.data.get(section,key)	#configparser的方法，获取配置文件中对应的值。section为XX.ini中[XX]部分。
		except:
			value = None
		return value

if __name__ == '__main__':
	read_ini = ReadIni()
	# smartPath()
	print(read_ini.get_value("MyBooksBanner","MyBooks"))
