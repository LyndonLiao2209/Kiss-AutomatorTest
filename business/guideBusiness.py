import time
from time import sleep
from handle.guideHandle import guideHandle
class guideBusiness:
	def __init__(self,i):
		# self.MyBooksHandle = base.base_driver(i)
		self.guideHandle = guideHandle(i)
	def lookBook(self):
		time.sleep(15)
		self.guideHandle.clickRead()
		pass






if __name__ == '__main__':
	guideBusiness = guideBusiness(0)
	guideBusiness.lookBook()

	sleep(15)
