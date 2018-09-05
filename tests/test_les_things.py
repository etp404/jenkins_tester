import unittest

from source.some_source import add


class ModelOptimisationTest(unittest.TestCase):

    # ported to libsnap
    def test_adder(self):
        self.assertEqual(4, add(2,2))