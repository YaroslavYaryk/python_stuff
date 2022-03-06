import unittest
from operator import add, truediv, mul, sub

def calculate(expression:str):
    allowed = "+-/*"
    storage = {
        "+" : add,
        "-" : sub,
        "*" : mul,
        "/" : truediv
    }
    if not any(i in expression for i in allowed):
        raise ValueError("text")

    a, b, sign = expression.split()

    return storage[sign](int(a), int(b))

class Tester(unittest.TestCase):

    def test_sign_exists(self):
        with self.assertRaises(ValueError) as e:
            calculate("1 2")
        self.assertEqual("text", e.exception.args[0])

    def test_add(self):
        self.assertEqual(calculate("1 2 +"), 3)

    def test_sub(self):
        self.assertEqual(calculate("1 2 -"), -1)

    def test_mul(self):
        self.assertEqual(calculate("1 2 *"), 2)

    def test_truediv(self):
        self.assertEqual(calculate("1 2 /"), 0.5)

    def test_less_than_3_parameters(self):
        with self.assertRaises(ValueError) as e:
            calculate("1 +")
        self.assertNotEqual('ok', e.exception.args[0])


if __name__ == "__main__":
    unittest.main()
