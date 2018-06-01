"""Provide unit tests for the translate.py script.

There are 3 test cases: a proper sentence, an improper sentence, and an empty sentence.

Usage:
    python test_translate.py

Output:
.This website has cookies to provide our services and show you relevant advertisements.
.We provide services and show related ads
.
----------------------------------------------------------------------
Ran 3 tests in 1.777s

OK

Author:
    Toan Luong, May 2018.
"""
import unittest
import warnings
import sys
sys.path.insert(0, '../')

from translate import translate

def ignore_warnings(test_func):
    """Turn off ResourceWarnings from Python during for unit tests.

    Args:
        test_func: test function

    Returns:
        do_test module

    Code from https://stackoverflow.com/questions/26563711/disabling-python-3-2-resourcewarning.
    """
    def do_test(self, *args, **kwargs):
        """Turn off any ResourceWarnings for test_func.
        """
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            test_func(self, *args, **kwargs)
    return do_test

class TestGTranslate(unittest.TestCase):
    """Unit Test Class for the translate.py script.
    
    There are 3 functions:
        test_translation()
        test_empty()
        test_sentence()
    """
    @ignore_warnings
    def test_translation(self):
        """Test for GTranslate smoothing of an improper sentence.
        """
        print(translate('Our services deliver and you to show relevant ads'))

    @ignore_warnings
    def test_empty(self):
        """Test for GTranslate smoothing of an empty sentence.
        """
        print(translate(''))

    @ignore_warnings
    def test_sentence(self):
        """Test for GTranslate smoothing of a proper sentence.
        """
        print(translate('This site have cookies to deliver our services \
            and to show you relevant ads.'))

if __name__ == '__main__':
    unittest.main()
