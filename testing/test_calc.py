



from PYTHON.calc import Calc
import pytest
import  yaml

def data():
    with open('test_data.yaml') as f:
        return  yaml.load(f)
class Test_calc:
    @classmethod
    def setup_class(cls):
        print('初始化类方法')
        cls.calc = Calc()
    # with open('test_data.yaml') as f:
    #     data = yaml.load(f)
    @pytest.mark.parametrize('a,b,c',data())
    def test_add(self,a,b,c):
        assert self.calc.add(a,b) == c
        print('执行add')

    if __name__ == '__main__':
        pytest.main('-v,-s')