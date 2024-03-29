import xlrd
from xlutils.copy import copy   #写数据不会清除旧数据，不能用xlwd
import os
# import sys
# from util.smartPath import smart
# smart =  smart()
# smart.smartPath()

parent_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
print(parent_path)
class OperaExcel:
	def __init__(self,file_path=None,i=None):
		if file_path == None:
			self.file_path = parent_path+'\config\case.xls'   #路径拼接，与环境变量解耦
		else:
			self.file_path = file_path	
		if i == None:
			i=0
		self.excel = self.get_excel()
		self.data = self.get_sheets(i)
			
	def get_excel(self):
		'''
		获取excel
		'''
		excel = xlrd.open_workbook(self.file_path)
		return excel

	def get_sheets(self,i):
		'''
		获取sheets的内容
		'''
		tables = self.excel.sheets()[i]
		return tables

	def get_lines(self):
		'''
		获取excel行数
		'''
		lines = self.data.nrows
		return lines

	def get_cell(self,row,cell):
		'''
		获取单元格内容
		'''
		data = self.data.cell(row,cell).value
		return data

	def write_value(self,row,value):
		read_value = self.excel
		write_data = copy(read_value)
		write_save = write_data.get_sheet(0)
		write_save.write(row,8,value)
		write_data.save(self.file_path)


if __name__ == '__main__':
	opera = OperaExcel()
	print("excel行数："+str(opera.get_lines()))
	print(opera.write_value(7,'pass'))



