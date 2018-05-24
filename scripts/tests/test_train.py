import unittest
import sys
import numpy as np

sys.path.insert(0, '../')

from utils import TextLoader

class TestUtilsMethods(unittest.TestCase):
    def setUp(self):
        self.data_loader = TextLoader("test_data", batch_size=2, seq_length=5)

    def test_init(self):
        print("Work in progress.")


if __name__ == '__main__':
    unittest.main()
