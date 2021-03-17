import unittest


class b_test(unittest.TestCase):
    def test_b(self):
        self.assertEqual(2, 3, "Another fail example")


if __name__ == '__main__':
    unittest.main()
