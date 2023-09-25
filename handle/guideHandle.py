#Bottom不属于任何页面，没有page和business
import time

from base.base_driver import BaseDriver
from page.guidePage import guidePage
class guideHandle:
	def __init__(self,i):
		self.guidePage = guidePage(i)
	#操作登录页面的元素
	def clickRead(self):
		'''
		点击阅读
		'''
		self.guidePage.getReadTheEntireStoryElement().click()



if __name__ =="__main__":

	time.sleep(20)