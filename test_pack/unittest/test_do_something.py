import unittest

from test_pack.libs import do_something


class TestDoSomething(unittest.TestCase):
    def test_main(self):
        result = do_something.main(1)
        self.assertEqual(2, result)


if __name__ == '__main__':
    unittest.main()
