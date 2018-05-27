from __future__ import print_function
import numpy as np
import tensorflow as tf

import argparse
import time
import os
from six.moves import cPickle

from utils import TextLoader
from model import Model
from eval import eval_str
from translate import translate

# Turn off Tensorflow debug output
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import warnings; warnings.simplefilter('ignore')

def main():
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
