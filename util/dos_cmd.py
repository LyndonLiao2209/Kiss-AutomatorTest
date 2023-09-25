#coding=utf-8
import os
import subprocess    #推荐使用

class DosCmd:
	def excute_cmd_result(self,command):
		result_list = []
		result = os.popen(command).readlines()
		# print(result)
		for i in result:  #去掉换行符
			if i =='\n':   #去掉换行符元素
				continue
			result_list.append(i.strip('\n'))
		return result_list

	def excute_cmd(self,command):
		try:
			print("appium启动的命令：",command)
			res = subprocess.run(command,shell=True,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE) #执行非0时抛异常
			print("执行成功："+ res.stdout.decode("gbk"))
		except  subprocess.CalledProcessError as err:
			print("执行失败："+ err.stderr.decode("gbk"))
		# os.system(command)


if __name__ == '__main__':
	dos = DosCmd()
	print(dos.excute_cmd_result('adb devices'))
	print(os.system('adb devices'))
