import sys
import os
fatherPath = os.path.abspath(os.path.join(os.getcwd(),".."))
sys.path.append(fatherPath)
from KeyWord.get_data import GetData
from KeyWord.action_method import ActionMethod
from util.server import Server


class RunMain:
	def run_method(self):
		server = Server()
		server.main()   #启动所有设备driver
		data = GetData()  #获取测试用例关键字
		action_method = ActionMethod()  #操作执行用例
		lines = data.get_case_lines()  #用例按步骤执行
		for i in range(1,lines):
			handle_step = data.get_handle_step(i)
			element_key = data.get_element_key(i)
			handle_value = data.get_handle_value(i)
			expect_key = data.get_expect_element(i)
			expect_step = data.get_expect_handle(i)
			#input()  login_button
			#input  str
			excute_method = getattr(action_method,handle_step)
			if element_key != None:      #有元素时操作元素
				excute_method(element_key,handle_value)
			else:   #无元素时操作值，如sleep
				excute_method(handle_value)
			if expect_step != None:    #期望断言
				expect_result = getattr(action_method,expect_step)
				result = expect_result(expect_key)
				if result:
					data.write_value(i,"passs")
				else:
					data.write_value(i,"fail")
			


if __name__ == '__main__':
	run = RunMain()
	run.run_method()
