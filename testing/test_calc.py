from PYTHON.calc import Calc


class Testcalc:
    def setup(self):
        self.calc = Calc()

    def test_add(self):
        assert self.calc.add(1, 2) == 3

    def test_add1(self):
        assert self.calc.add(-1, 3) == 2

    def test_add2(self):
        assert self.calc.add(-1, -2) == -3

    def test_add3(self):
        assert self.calc.add(0, 0) == 0

    def test_div1(self):
        assert self.calc.div(0, 1) == 0

    def test_div2(self):
        assert self.calc.div(3, 1.5) == 2

    def test_div(self):
        assert self.calc.div(1, 2) == 0.5

    def test_mul(self):
        assert self.calc.mul(1, 2) == 2

    def test_sub(self):
        assert self.calc.sub(0, 0) == 0






