"""Provide unit tests for the eval.py script.

There are 2 types of test inputs: with an input .txt file and an input String.
The goal of eval.py is to deliver the grammar score of a given .txt or String.

Require:
    pip install language-check

Author:
    Toan Luong, May 2018.
"""
import unittest

from fakereviewgenerator.eval import eval_txt, eval_str

class TestEvalMethods(unittest.TestCase):
    """Unit Test Class for the eval.py script.
    There are 2 functions:
        test_sample_file()
        test_empty_file()
        test_str()
        test_empty_str()
    """
    def test_sample_file(self):
        """Test if input is a .txt file. Located in the data/tests/test_data directory.
        """
        self.assertTrue(eval_txt('data/test_data/word-rnn-output.txt', verbose=True)[0] > 0)

    def test_empty_file(self):
        """Test if input is a non-existed .txt file.
        """
        with self.assertRaises(Exception): eval_txt('eh.txt', verbose=False)

    def test_str(self):
        """Test if input is an improper String.
        """
        example = "This site have cookies to deliver our services and to show you \
        relevant ads and job listings. And I asd"
        self.assertTrue(eval_str(example, verbose=True)[0] > 0)

    def test_empty_str(self):
        """Test if input is an empty String.
        """
        with self.assertRaises(Exception): eval_str('', verbose=True)

if __name__ == '__main__':
    unittest.main()
