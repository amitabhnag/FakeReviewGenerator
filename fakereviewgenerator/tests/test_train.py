"""Provide unit tests for the train.py script.

Run TextLoader and train the model.

Usage:
    python test_train.py

test_data/input.txt

this is cat
I love cat very much
cat loves me

Output:

reading text file
Work in progress.
.
----------------------------------------------------------------------
Ran 1 test in 0.007s
OK

Code from https://github.com/hunkim/word-rnn-tensorflow.
"""
import unittest
import sys

from utils import TextLoader

class TestUtilsMethods(unittest.TestCase):
    """Unit Test Class for the utils.py script.
    There are 2 functions:
        setUp()
        test_init()
        test_build_vocab()
        test_batch_vocab()
    """
    def setUp(self):
        """Initialize the data_loader object as the TextLoader class with
        input from test_data/input.txt.
        """
        self.data_loader = TextLoader("test_data", batch_size=2, seq_length=5)

    def test_init(self):
        """Print message.
        """
        print("Work in progress.")

if __name__ == '__main__':
    unittest.main()
