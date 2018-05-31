""" This module generates a sample text from a trained model. It then
smoothens the text by using google translate to convert sample text
from English to Chinese and back to English. This module runs
grammar check to objectively evaluate the quality of sample text

Functions:
main: This main() function starts the sampling process. User arguments are
    parsed and stored in a parser object. parser object is passed
    to the sample() function to begin model training
sample: Function to sample from a given an input model. After sampling this
    function can run google translate smoothing. This smoothing is
    achieved by first translating sample text from English to Chinese and
    then from Chinese back to English. This function also runs a grammar
    check on the sample text to objectively assess the quality of sampled
    output.
"""
from __future__ import print_function

import argparse
import time
import os

import numpy as np
import tensorflow as tf

from six.moves import cPickle
from utils import TextLoader
from model import Model
from eval import eval_str
from translate import translate

# Turn off Tensorflow debug output
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import warnings; warnings.simplefilter('ignore')

def main():
    """ This main() function starts the sampling process. User arguments are
    parsed and stored in a parser object. parser object is passed
    to the sample() function to begin model training

    Arguments (default values):
    --save_dir: model directory to load stored checkpointed models
                from(save)
    --n: number of words to sample (200)
    --prime: prime text (' ')
    --pick: 1 = weighted pick, 2 = beam search pick (1)
    --width: width of the beam search (4)
    --sample: 0 to use max at each timestep, 1 to sample at
              each timestep, 2 to sample on spaces (1)
    --count: number of samples to print (1)
    --quiet: suppress printing the prime text (false)
    --show_grammar: show grammatical errors of the generated review
                    (false)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_dir', type=str, default='save',
                        help='model directory to load stored checkpointed models from')
    parser.add_argument('-n', type=int, default=200,
                        help='number of words to sample')
    parser.add_argument('--prime', type=str, default=' ',
                        help='prime text')
    parser.add_argument('--pick', type=int, default=1,
                        help='1 = weighted pick, 2 = beam search pick')
    parser.add_argument('--width', type=int, default=4,
                        help='width of the beam search')
    parser.add_argument('--sample', type=int, default=1,
                        help='0 to use max at each timestep, 1 to sample at \
                        each timestep, 2 to sample on spaces')
    parser.add_argument('--count', '-c', type=int, default=1,
                        help='number of samples to print')
    parser.add_argument('--quiet', '-q', default=False, action='store_true',
                        help='suppress printing the prime text (default false)')
    parser.add_argument('--show_grammar', '-g', default=False, action='store_true',
                        help='show grammatical errors of the generated review (default false)')

    args = parser.parse_args()
    sample(args)

def sample(args):
    """
    Function to sample from a given an input model. After sampling this
    function can run google translate smoothing. This smoothing is
    achieved by first translating sample text from English to Chinese and
    then from Chinese back to English. This function also runs a grammar
    check on the sample text to objectively assess the quality of sampled
    output.

    Parameter:
        args: User provided or default value of arguments received
        from the main function
    """
    with open(os.path.join(args.save_dir, 'config.pkl'), 'rb') as f:
        saved_args = cPickle.load(f)
    with open(os.path.join(args.save_dir, 'words_vocab.pkl'), 'rb') as f:
        words, vocab = cPickle.load(f)
    model = Model(saved_args, True)
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        saver = tf.train.Saver(tf.global_variables())
        ckpt = tf.train.get_checkpoint_state(args.save_dir)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            for _ in range(args.count):
                output = model.sample(sess, words, vocab, args.n, args.prime,
                                      args.sample, args.pick,
                                      args.width, args.quiet)
                score, matches = eval_str(output)
                print("===== Before GTranslate Smoothing. Grammar Score = %i" %score)
                print(output)
                gtranslate_output = translate(output)
                new_score, new_matches = eval_str(gtranslate_output)
                print("===== After GTranslate Smoothing. Grammar Score = %i" %new_score)
                print(translate(gtranslate_output))
                if args.show_grammar:
                    for err in matches:
                        print("---")
                        print(err)

if __name__ == '__main__':
    main()
