from PYTHON.calc import Calc
import pytest
import yaml


def steps_data():
    with open('test_steps.yaml') as i:
        return yaml.load(i)


class Test_calc:
    @classmethod
    def setup_class(cls):
        print('初始化类方法')
        cls.calc = Calc()

    with open('test_data.yaml') as f:
        data = yaml.load(f)

    @pytest.mark.parametrize('a,b,c', data)
    def test_step(self, a, b, c):
        steps = steps_data()
        for step in steps:
            if step == 'add':
                print('执行add方法')
                assert self.calc.add(a, b) == c
            elif step == 'div':
                print('执行div方法')
                assert self.calc.div(a, b) == c

    if __name__ == '__main__':
        pytest.main('-v,-s')
