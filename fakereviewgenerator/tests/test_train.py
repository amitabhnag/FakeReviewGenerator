"""Provide unit tests for the train.py and sample.py script.

Inside the test_data/pitchfork_test, there is input.txt as 1MB text file to train the model.
The tests will attempt to train the model for 1 epoch and sample a fake music review with a 
random seed word.

Usage:
    python test_train.py

Author: Toan Luong, May 2018.
"""
import unittest
import os
import warnings
import time
from fakereviewgenerator.utils import TextLoader
from fakereviewgenerator.train import create_train_parser, train
from fakereviewgenerator.sample import create_sample_parser, sample

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
        """Set up various training and sampling parameters.
        """
        test_log_dir = '.test_logs'
        test_save_dir = '.test_save'
        if not os.path.exists(test_log_dir):
            os.makedirs(test_log_dir)
        if not os.path.exists(test_save_dir):
            os.makedirs(test_save_dir)
        self.train_params = create_train_parser(['--data_dir=data/test_data/pitchfork_test', '--log_dir=%s' %(test_log_dir),
            '--save_dir=%s' %(test_save_dir), '--model=gru', '--num_epochs=1', '--batch_size=100', '--gpu_mem=0.8'])
        self.sample_params = create_sample_parser(['--save_dir=%s'%(self.train_params.save_dir)])

    @ignore_warnings
    def test_train(self):
        """Test the train and sample loop.
        """
        print("Begin training for 1 epoch for the file %s..." %self.train_params.data_dir)
        start = time.time()
        train(self.train_params)
        print("Finished training with after time = %0.3f!" %(time.time()-start))

        print("Begin sampling with random seed word ...")
        sample(self.sample_params)
        print("Finished sampling!")
        
        print("Begin sampling with beam search pick ...")
        self.sample_params.pick = 2
        sample(self.sample_params)
        print("Finished sampling!")

        print("Begin sampling with max at each time step ...")
        self.sample_params.sample = 0
        sample(self.sample_params)
        print("Finished sampling!")

        print("Begin sampling with spaces ...")
        self.sample_params.sample = 2
        sample(self.sample_params)
        print("Finished sampling!")

        print("Begin sampling with prime word 'why not' ...")
        self.sample_params.pick = 1
        self.sample_params.prime = 'why not'
        self.sample_params.show_grammar = True
        self.sample_params.sample = 1
        sample(self.sample_params)
        print("Finished sampling!")

        self.assertTrue(self.sample_params.save_dir == self.train_params.save_dir)

if __name__ == '__main__':
    unittest.main()
