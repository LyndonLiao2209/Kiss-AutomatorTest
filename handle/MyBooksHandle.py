from page.MyBooksPage import MyBooksPage
from time import sleep
class MyBooksHandle:
	def __init__(self,i):
		self.MyBooksPage = MyBooksPage(i)
	#操作登录页面的元素
	def clickBanner(self):
		'''
		点击banner图
		'''
		self.MyBooksPage.getMyBooksBannerElement().click()




if __name__ == "__main__":
	handle = MyBooksHandle(1)
	sleep(6)
	handle.clickBanner()