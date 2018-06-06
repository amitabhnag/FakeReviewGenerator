"""Provide unit tests for the translate.py script.

There are 3 test cases: a proper sentence, an improper sentence, and an empty sentence.

Author:
    Toan Luong, May 2018.
"""
import unittest
import warnings

from FakeReviewGenerator.translate import translate

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
        out = translate('Our services deliver and you to show relevant ads')
        print(out)
        self.assertTrue(len(out) > 0)

    @ignore_warnings
    def test_empty(self):
        """Test for GTranslate smoothing of an empty sentence.
        """
        self.assertTrue(len(translate('')) == 0)

    @ignore_warnings
    def test_sentence(self):
        """Test for GTranslate smoothing of a proper sentence.
        """
        out = translate('This site have cookies to deliver our services \
            and to show you relevant ads')
        print(out)
        self.assertTrue(len(out) > 0)

if __name__ == '__main__':
    unittest.main()
