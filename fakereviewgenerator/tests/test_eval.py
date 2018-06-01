"""Provide unit tests for the eval.py script.

There are 2 types of test inputs: with an input .txt file and an input String.
The goal of eval.py is to deliver the grammar score of a given .txt or String.

Require:
    pip install language-check

Usage:
    python test_eval.py

Output:
Line 1, column 488, Rule ID: MORFOLOGIK_RULE_EN_US
Message: Possible spelling mistake found
Suggestion: in; is; I; it; him; if; km; FM; am; cm; mm; IBM; Jim;
PM; pm; rim; ID; IQ; id; IMF; dim; IMO; um; imp; aim; gm; vim; GM; Kim;
Tim; AM; Am; BM; Cm; EM; Fm; HM; IA; IE; IL; IN; IT;
IV; Ia; In; Io; Ir; It; M; MM; NM; Pm; QM; Sm; TM; Tm; Wm; em; i; ii;
ism; iv; ix; m; mi; om; rm; i m
...f the jam vocal guitar shouts and cries im not really there evokes the course of l...
                                           ^^
19
.Line 1, column 101, Rule ID: MORFOLOGIK_RULE_EN_US
Message: Possible spelling mistake found
Suggestion: and; as; add; aid; ad; ask; ads; ash; SD; eyed; sad; BSD; LSD;
AD; ADD; asp; ASL; As; ass; as d
...ou relevant ads and job listings. And I asd
                                           ^^^
1
.
======================================================================
ERROR: test_empty_file (__main__.TestEvalMethods)
Test if input is a .txt file. Located in the tests/test_data directory.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_eval.py", line 41, in test_empty_file
    print(eval_txt('eh.txt', verbose=True)[0])
  File "../eval.py", line 26, in eval_txt
    raise OSError("File Not Found")
OSError: File Not Found

======================================================================
ERROR: test_empty_str (__main__.TestEvalMethods)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_eval.py", line 46, in test_empty_str
    print(eval_str('', verbose=True)[0])
  File "../eval.py", line 46, in eval_str
    raise ValueError("String is empty")
ValueError: String is empty

----------------------------------------------------------------------
Ran 4 tests in 1.795s

FAILED (errors=2)

Author:
    Toan Luong, May 2018.
"""
import unittest
import sys
sys.path.insert(0, '../')

from eval import eval_txt, eval_str

class TestEvalMethods(unittest.TestCase):
    """Unit Test Class for the eval.py script.
    There are 2 functions:
        test_sample_file()
        test_empty_file()
        test_str()
        test_empty_str()
    """
    def test_sample_file(self):
        """Test if input is a .txt file. Located in the tests/test_data directory.
        """
        print(eval_txt('test_data/word-rnn-output.txt', verbose=True)[0])

    def test_empty_file(self):
        """Test if input is a non-existed .txt file.
        """
        print(eval_txt('eh.txt', verbose=True)[0])

    def test_str(self):
        """Test if input is an improper String.
        """
        example = "This site have cookies to deliver our services and to show you \
        relevant ads and job listings. And I asd"
        print(eval_str(example, verbose=True)[0])

    def test_empty_str(self):
        """Test if input is an empty String.
        """
        print(eval_str('', verbose=True)[0])

if __name__ == '__main__':
    unittest.main()
