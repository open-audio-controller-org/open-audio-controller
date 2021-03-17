import unittest


class a_test(unittest.TestCase):
    def test_a(self):
        self.assertEqual(1, 2, "Fail Example")


if __name__ == '__main__':
    unittest.main()
