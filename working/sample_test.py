import unittest
import os

class TestFakeReviews(unittest.TestCase):
    def test_path_exists(self):
        """Test if output .txt file exists
        """
        self.assertTrue(os.path.exists('output.txt'))

    def test_char_len(self):
        """Test the output file to have less than or equal to 1000 characters
        """
        with open ("output.txt", "r") as f:
            data = f.read().replace('\n', '')
        self.assertTrue(len(data) <= 1000)

    def test_special_chars(self, seed_word='music'):
        """Test if the default seed_word music is in the output file
        """
        with open ("output.txt", "r") as f:
            data = f.read().replace('\n', '')
        self.assertTrue(seed_word in data)

if __name__ == '__main__':
    unittest.main()