import yaml
import os
import sys
fatherPath = os.path.abspath(os.path.join(os.getcwd(), ".."))
sys.path.append(fatherPath)
'''
读写yaml文件(设备信息)
'''
class WriteUserCommand:
	def read_data(self):
		'''
		加载yaml数据
		'''
		with open("../config/userconfig.yaml") as fr:
			data = yaml.safe_load(fr)
			print(data)
		return data

	def get_value(self,key,port=None):  #获取设备和设备属性。如：{'user_info_1': {'bp': '4789', 'deviceName': 'R9PRB0EY45W', 'port': '4723'}}
		#key = 'user_info_1';port为bp/port/deviceName等
		'''
		获取value
		'''
		data = self.read_data()
		print("yaml data is: "+str(data))

		value = data[key][port]
		# value = data[key]
		print("yaml value is: "+ str(value))
		return value

	def write_data(self,i,device,bp,port):
		'''
		写入设备信息到yaml文件中
		'''
		data = self.join_data(i,device,bp,port)
		with open("../config/userconfig.yaml","a") as fr:
			yaml.dump(data,fr)

	def join_data(self,i,device,bp,port):
		'''
		按照格式写入设备信息
		'''
		data = {
		"user_info_"+str(i):{
		"deviceName":device,
		"bp":bp,
		"port":port
		}
		}
		print(type(data))
		return data

	def clear_data(self):
		with open("../config/userconfig.yaml","w") as fr:
			fr.truncate()  #清空yaml以便重新写入
		fr.close()

	def get_file_lines(self):
		data = self.read_data()
		return len(data)


if __name__ == '__main__':
	write_file = WriteUserCommand()
	write_file.write_data(0,'deviceName','bp','port')
	# print(write_file.get_value('user_info_1','deviceName'))
