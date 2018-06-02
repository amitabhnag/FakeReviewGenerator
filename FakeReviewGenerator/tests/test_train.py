"""Provide unit tests for the train.py and sample.py script.

Inside the test_data/pitchfork_test, there is input.txt as 1MB text file to train the model.
The tests will attempt to train the model for 1 epoch and sample a fake music review with a 
random seed word. 

Usage:
    python test_train.py

Author: Toan Luong, May 2018.
"""
import unittest
import sys
import os
import warnings

from utils import TextLoader
from train import train
from sample import sample

class TrainParams:
    """TrainParams class stores various training configurations.
    """
    def __init__(self, data_dir='test_data/pitchfork_test', input_encoding=None, log_dir='.test_logs',
        save_dir='.test_save', rnn_size=256, num_layers=2, model='lstm', batch_size=100,
        seq_length=25, num_epochs=1, save_every=1000, grad_clip=5., learning_rate=0.002,
        decay_rate=0.97, gpu_mem=0.8, init_from=None):
        """Initialize the class with default configurations for easier testing.
        """
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        self.data_dir = data_dir
        self.input_encoding = input_encoding
        self.log_dir = log_dir
        self.save_dir = save_dir
        self.rnn_size = rnn_size
        self.num_layers = num_layers
        self.model = model
        self.batch_size = batch_size
        self.seq_length = seq_length
        self.num_epochs = num_epochs
        self.save_every = save_every
        self.grad_clip = grad_clip
        self.learning_rate = learning_rate
        self.decay_rate = decay_rate
        self.gpu_mem = gpu_mem
        self.init_from = init_from

class SampleParams:
    """SampleParams class stores various sampling configurations.
    """
    def __init__(self, save_dir, n=200, prime='', pick=1, width=4, sample=1, count=1, quiet=False, show_grammar=True):
        """Initialize the class with default configurations for easier testing.
        """
        self.save_dir = save_dir
        self.n = n
        self.prime = prime
        self.pick = pick
        self.width = width
        self.sample = sample
        self.count = count
        self.quiet = quiet
        self.show_grammar = show_grammar

def ignore_warnings(test_func):
    """Turn off ResourceWarnings and DeprecationWarning from Python during for unit tests.

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
            warnings.simplefilter("ignore", DeprecationWarning)
            warnings.simplefilter("ignore", ResourceWarning)
            test_func(self, *args, **kwargs)
    return do_test

class TestUtilsMethods(unittest.TestCase):
    """Unit Test Class for the utils.py script.
    There are 2 functions:
        setUp()
        test_init()
        test_build_vocab()
        test_batch_vocab()
    """
    @ignore_warnings
    def setUp(self):
        """Set up various training parameters.
        
        Assign the save_dir 
        """
        self.train_params = TrainParams()
        self.sample_params = SampleParams(save_dir=self.train_params.save_dir)

    @ignore_warnings
    def test_train(self):
        """Test the train and sample loop.
        """
        print("Begin training for 1 epoch for the file %s..." %self.train_params.data_dir)
        train(self.train_params)
        print("Finished training!")
        print("Begin sample from the save_dir %s..." %self.sample_params.save_dir)
        sample(self.sample_params)
        print("Finished sampling!")

if __name__ == '__main__':
    unittest.main()
