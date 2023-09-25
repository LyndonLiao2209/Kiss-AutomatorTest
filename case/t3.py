import os
import sys
import pytest
import pytest_html
import threading
from util.server import Server

# 定义一个 pytest 测试用例类
class TestAPP:

    # 标记一个测试用例
    @pytest.mark.parametrize("input, expected", [("hello", "HELLO"), ("world", "WORLD")])
    def test_uppercase(self, input, expected):
        result = input.upper()
        assert result == expected

    # 标记另一个测试用例
    def test_addition(self):
        assert 2 + 2 == 4



# 添加测试套件
def get_test_suite():
    suite = pytest.TestSuite()

    # 创建一个测试加载器
    loader = pytest.loader.TestLoader()

    # 添加指定类中的所有测试方法到测试套件中
    suite.addTests(loader.loadTestsFromTestCase(TestMyApp))

    return suite


# 运行测试套件
if __name__ == "__main__":
    runner = pytest.TextTestRunner()
    suite = get_test_suite()
    runner.run(suite)



# def get_suite(i):
#
#     suite = unittest.TestSuite()
#
#     suite.addTest(CaseTest("test_01", param=i))
#
#     suite.addTest(CaseTest("test_02", param=i))
#
#     unittest.TextTestRunner().run(suite)



# if __name__ == '__main__':
#     pass

    # threads = []
    #
    # for i in range(5):
    #
    #     print(">>>>>>>>>>>>>>"+str(i))
    #
    #     t = threading.Thread(target=get_suite, args=(i,))
    #
    #     threads.append(t)
    #
    # for j in threads:
    #
    #     j.start()