import unittest
import sys
sys.path.insert(0, '../')

from eval import *

class TestEvalMethods(unittest.TestCase):
	def test_sample_file(self):
		eval_txt('test_data/word-rnn-output.txt')

	def test_na_file(self):
		eval_txt('test_data/a.txt')

	def test_str(self):
		s = 'This site have cookies to deliver our services and to show you relevant ads and job listings. By use our site, you acknowledge that you have read and understand our Cookie Policy, Privacy Policy, and our Terms of Service.'
		eval_str(s, verbose=True)

if __name__ == '__main__':
	unittest.main()
