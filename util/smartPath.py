#coding=utf-8
import os
import sys
class smart:
	def __init__(self):
		self.currentPath = os.getcwd()
	def smartPath(self):  # 智能设置path
		tmpList = self.currentPath.split("\\")
		# print(tmpList)
		if tmpList[-1] == 'Kiss-AutomatedTest':
			sys.path.append(self.currentPath)
		elif tmpList[-2] == 'Kiss-AutomatedTest':
			fatherPath = os.path.dirname(self.currentPath)
			sys.path.append(fatherPath)  # 添加父节点为代码路径。append无返回值，添加后可通过path查看
		# return sys.path


if __name__ == '__main__':
	smart = smart()
	smart.smartPath()
	print(sys.path)