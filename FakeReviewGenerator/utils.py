"""
Provide utilities functions to support train.py.
The class TextLoader() provides capabilities to load a .txt text corpus to create
a vocab.pkl and create batches of Numpy tensors to feed into the neural network.

Example:
    from utils import TextLoader
    data_loader = TextLoader(data_dir, batch_size, seq_length, encoding)

Code from https://github.com/hunkim/word-rnn-tensorflow
"""
import os
import codecs
import collections
from six.moves import cPickle
import numpy as np
import re
import itertools

class TextLoader():
    """Process the input text file and contain tensor information to feed in the neural network.
    
    Functions:
        clean_str
        build_vocab
        preprocess
        load_preprocessed
        create_batches
        reset_batch_pointer

    Attributes:
        data_dir: directory to store input .txt file.
        batch_size: batch_size to be fed in the network.
        seq_length: sequence length.
        vocab: vocabulary mapping.
        vocab_size: number of words in the vocab corpus.
        tensor: input tensor.
        pointer: pointer to keep track of data batches.
        x_batches: batches of features
        y_batches: batches of labels
    """
    def __init__(self, data_dir, batch_size, seq_length, encoding=None):
        """Initialzize the TextLoader class. 
        
        Check data directory if vocab.pkl and data.npy files already existed.
        Create batches of features and labels from the batch information and tensors.
        Set batch pointer to 0.

        Args:
            data_dir: directory to store input.txt, vocab.pkl, and data.npy.
            batch_size: size of tensor batches to feed into the net.
            seq_length: length of embedding sequence.
            encoding: encoding type of the input text file. Default None.
        """
        self.data_dir = data_dir
        self.batch_size = batch_size
        self.seq_length = seq_length

        input_file = os.path.join(data_dir, "input.txt")
        vocab_file = os.path.join(data_dir, "vocab.pkl")
        tensor_file = os.path.join(data_dir, "data.npy")

        # Let's not read voca and data from file. We many change them.
        if True or not (os.path.exists(vocab_file) and os.path.exists(tensor_file)):
            print("reading text file")
            self.preprocess(input_file, vocab_file, tensor_file, encoding)
        else:
            print("loading preprocessed files")
            self.load_preprocessed(vocab_file, tensor_file)
        self.create_batches()
        self.reset_batch_pointer()

    def clean_str(self, string):
        """Tokenization/string cleaning for all datasets except for SST.
        
        Code from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.

        Args:
            string: input string.

        Returns:
            clean version of the original string and lower-cased.
        """
        string = re.sub(r"[^가-힣A-Za-z0-9(),!?\'\`]", " ", string)
        string = re.sub(r"\'s", " \'s", string)
        string = re.sub(r"\'ve", " \'ve", string)
        string = re.sub(r"n\'t", " n\'t", string)
        string = re.sub(r"\'re", " \'re", string)
        string = re.sub(r"\'d", " \'d", string)
        string = re.sub(r"\'ll", " \'ll", string)
        string = re.sub(r",", " , ", string)
        string = re.sub(r"!", " ! ", string)
        string = re.sub(r"\(", " \( ", string)
        string = re.sub(r"\)", " \) ", string)
        string = re.sub(r"\?", " \? ", string)
        string = re.sub(r"\s{2,}", " ", string)
        return string.strip().lower()

    def build_vocab(self, sentences):
        """Builds a vocabulary mapping from word to index based on the sentences.

        Args:
            sentences: input text paragraph consists of multiple words.

        Returns:
            [vocabulary mapping, inverse vocabulary mapping]
        """
        # Build vocabulary
        word_counts = collections.Counter(sentences)
        # Mapping from index to word
        vocabulary_inv = [x[0] for x in word_counts.most_common()]
        vocabulary_inv = list(sorted(vocabulary_inv))
        # Mapping from word to index
        vocabulary = {x: i for i, x in enumerate(vocabulary_inv)}
        return [vocabulary, vocabulary_inv]

    def preprocess(self, input_file, vocab_file, tensor_file, encoding):
        """Given an input text file, generate arrays of tensors.

        Args:
            input_file: input text file.
            vocab_file: where to store the vocab.pkl file.
            tensor_file: where to store the data.npy file.
            encoding: encoding config to read the text file if any.
        """
        with codecs.open(input_file, "r", encoding=encoding) as f:
            data = f.read()

        # Optional text cleaning or make them lower case, etc.
        # data = self.clean_str(data)
        x_text = data.split()

        self.vocab, self.words = self.build_vocab(x_text)
        self.vocab_size = len(self.words)

        with open(vocab_file, 'wb') as f:
            cPickle.dump(self.words, f)

        # The same operation like this [self.vocab[word] for word in x_text]
        # index of words as our basic data
        self.tensor = np.array(list(map(self.vocab.get, x_text)))
        # Save the data to data.npy
        np.save(tensor_file, self.tensor)

    def load_preprocessed(self, vocab_file, tensor_file):
        """Load vocab.pkl and data.npy if the input text file has already been processed.

        Args:
            vocab_file: where to store the vocab.pkl file.
            tensor_file: where to store the data.npy file.
        """
        with open(vocab_file, 'rb') as f:
            self.words = cPickle.load(f)
        self.vocab_size = len(self.words)
        self.vocab = dict(zip(self.words, range(len(self.words))))
        self.tensor = np.load(tensor_file)
        self.num_batches = int(self.tensor.size / (self.batch_size *
                                                   self.seq_length))

    def create_batches(self):
        """From the batch information and features tensors, create batches of features and
        labels to feed in the neural network.
        """
        self.num_batches = int(self.tensor.size / (self.batch_size *
                                                   self.seq_length))
        if self.num_batches == 0:
            assert False, "Not enough data. Make seq_length and batch_size small."

        self.tensor = self.tensor[:self.num_batches * self.batch_size * self.seq_length]
        xdata = self.tensor
        ydata = np.copy(self.tensor)

        ydata[:-1] = xdata[1:]
        ydata[-1] = xdata[0]
        self.x_batches = np.split(xdata.reshape(self.batch_size, -1), self.num_batches, 1)
        self.y_batches = np.split(ydata.reshape(self.batch_size, -1), self.num_batches, 1)

    def next_batch(self):
        """Given the current pointer, load the next batch of the x_batches and y_batches lists.
        """
        x, y = self.x_batches[self.pointer], self.y_batches[self.pointer]
        self.pointer += 1
        return x, y

    def reset_batch_pointer(self):
        """Reset batch pointer to 0
        """
        self.pointer = 0
