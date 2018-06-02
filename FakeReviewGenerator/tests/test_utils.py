"""Provide unit tests for the translate.py script.

After initialization of the TextLoader class, the unit tests check for:
    - Attributes: vocab, tensor, vocab_size
    - Integrity of the vocab mapping
    - Lengths of features needs to match those of labels/targets.

Usage:
    python test_utils.py

test_data/input.txt

this is cat
I love cat very much
cat loves me

Output:

reading text file
(1, 2, 5)
.reading text file
{'I': 0, 'cat': 1, 'love': 2} ['I', 'cat', 'love']
.reading text file
{'I': 0, 'cat': 1, 'is': 2, 'love': 3, 'loves': 4, 'me': 5, 'much': 6, 'this': 7, 'very': 8}
[7 2 1 0 3 1 8 6 1 4]
9
.
----------------------------------------------------------------------
Ran 3 tests in 0.057s
OK

Code from https://github.com/hunkim/word-rnn-tensorflow.
"""
import unittest
from collections import Counter
import numpy as np

from utils import TextLoader

class TestUtilsMethods(unittest.TestCase):
    """Unit Test Class for the utils.py script.
    There are 4 functions:
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
        """Print out the 3 main attributes of TextLoader. Make sure they match with (1, 2, 5).
        """
        print(self.data_loader.vocab)
        print(self.data_loader.tensor)
        print(self.data_loader.vocab_size)

    def test_build_vocab(self):
        """Test for vocab dictionary matches {'I': 0, 'love': 2, 'cat': 1}.
        """
        sentences = ["I", "love", "cat", "cat"]
        vocab, vocab_inv = self.data_loader.build_vocab(sentences)
        print(vocab, vocab_inv)
        # Must include I, love, and cat
        self.assertEqual(Counter(list(vocab)), Counter(list(["I", "love", "cat"])))
        self.assertDictEqual(vocab, {'I': 0, 'love': 2, 'cat': 1})

        self.assertEqual(Counter(list(vocab_inv)), Counter(list(["I", "love", "cat"])))

    def test_batch_vocab(self):
        """Test for the length of x_batches need to match that of y_batches.
        """
        print(np.array(self.data_loader.x_batches).shape)
        self.assertEqual(Counter(list(self.data_loader.x_batches[0][0][1:])),
                         Counter(list(self.data_loader.y_batches[0][0][:-1])))
        self.assertEqual(Counter(list(self.data_loader.x_batches[0][1][1:])),
                         Counter(list(self.data_loader.y_batches[0][1][:-1])))

    def test_clean_str(self):
        print(self.data_loader.clean_str("@$)@(toaNs24luoNG"))

if __name__ == '__main__':
    unittest.main()
