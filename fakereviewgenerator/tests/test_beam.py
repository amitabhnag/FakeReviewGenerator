"""Provide unit tests for the beam.py script.

Usage:
    python test_beam.py

Output:
----------------------------------------------------------------------
Ran 2 tests in 0.001s
OK

Code from https://github.com/hunkim/word-rnn-tensorflow.
"""
import sys
import unittest
import numpy as np

from beam import BeamSearch

def naive_predict(sample, state):
    """Fake predict function.

    For our model, let's assume a vocabulary of size 5. Furthermore, let's say
    that the `state` is exactly the probability that each vocabulary occurs,
    and these probabilities never change.

    Args:
        sample
        state

    Returns:
        all elements in state.

    """
    return np.array(state)[None, :], state

class TestBeamMethods(unittest.TestCase):
    """Unit Test Class for the utils.py script.
    There are 2 functions:
        setUp()
        test_init()
        test_build_vocab()
        test_batch_vocab()

    Attributes:
        prime_labels
        initial_state
    """
    def setUp(self):
        """Set up 2 attributes.
        """
        self.prime_labels = [0, 1]
        self.initial_state = [0.1, 0.2, 0.3, 0.4, 0.5]

    def test_single_beam(self):
        """Test for single beam.
        """
        beams = BeamSearch(naive_predict, self.initial_state, self.prime_labels)
        samples, _ = beams.search(None, None, k=1, maxsample=5)
        self.assertEqual(samples, [[0, 1, 4, 4, 4]])

    def test_multiple_beams(self):
        """Test for multiple beams.
        """
        beams = BeamSearch(naive_predict, self.initial_state, self.prime_labels)
        samples, scores = beams.search(None, None, k=4, maxsample=5)
        self.assertIn([0, 1, 4, 4, 4], samples)
        # All permutations of this form must be in the results.
        self.assertIn([0, 1, 4, 4, 3], samples)
        self.assertIn([0, 1, 4, 3, 4], samples)
        self.assertIn([0, 1, 3, 4, 4], samples)
        # Make sure that the best beam has the lowest score.
        self.assertEqual(samples[np.argmin(scores)], [0, 1, 4, 4, 4])

if __name__ == '__main__':
    unittest.main()
