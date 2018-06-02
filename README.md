## Fake Review Generator

[![Build Status](https://travis-ci.org/amitabhnag/FakeReviewGenerator.svg?branch=master)](https://travis-ci.org/amitabhnag/FakeReviewGenerator)
[![Coverage Status](https://coveralls.io/repos/github/amitabhnag/FakeReviewGenerator/badge.png?branch=master&service=github)](https://coveralls.io/github/amitabhnag/FakeReviewGenerator?branch=master)


This project is all about trying to train a word recurrent neural network using Tensorflow.

The data that we use is publicly available and comes from two popular sites, Amazon and Pitchfork, and is a collection of 
user reviews posted on them.

Our goal is to train our model using this data, so as to generate reviews that resemble actual user reviews.

Inspired by [word-rnn](https://github.com/hunkim/word-rnn-tensorflow) and

Andrej Karpathy's [char-rnn](https://github.com/karpathy/char-rnn).

## Getting Started

All the python files are inside the /fakereviewgenerator folder.

### Installation

The python file `setup.py` will ensure the required packages are installed in the local environment. 

### Prerequisites

- [Tensorflow 1.0](http://www.tensorflow.org)

### Basic Usage

To train with default parameters on the pitchfork dataset, run `python train.py`. 

To access all the parameters use `python train.py --help`.

To sample from a checkpointed model, `python sample.py`.

To train and sample together, use the shell script `demo.sh`. The file takes 2 parameters, no of epochs and seed to sample with.

For each epoch trained, an output will be printed, so one can see the model getting better as the training progresses.

The `_sample.py_` file, also includes a grammer check and google translate module as a post processing step.

One can see the grammer check score, and the output quality improving as the training proceeds. 

Sampling while the learning is still in progress (to check last checkpoint) works only in CPU or using another GPU.
To force CPU mode, use `export CUDA_VISIBLE_DEVICES=""` and `unset CUDA_VISIBLE_DEVICES` afterward
(resp. `set CUDA_VISIBLE_DEVICES=""` and `set CUDA_VISIBLE_DEVICES=` on Windows).

To continue training after interruption or to run on more epochs, `python train.py --init_from=save`

### Datasets

You can use any plain text file as input. To run `python train.py` with a different file, either replace the existing input file inside
`./data/pitchfork/`, which is the default directory, or run the code as

 `python train.py --data_dir=./data/yourfolder/input.txt`.

 A quick tip to concatenate many small disparate `.txt` files into one large training file: `ls *.txt | xargs -L 1 cat >> input.txt`.

Two datasets were used in this project. One is from Amazon(https://www.kaggle.com/snap/amazon-fine-food-reviews/data)

and the other is from Pitchfork(https://www.kaggle.com/nolanbconaway/pitchfork-data/data).

### Tuning

Tuning your models is kind of a "dark art" at this point. In general:

1. Start with as much clean input.txt as possible e.g. 50MiB
2. Start by establishing a baseline using the default settings.
3. Use tensorboard to compare all of your runs visually to aid in experimenting.
4. Tweak --rnn_size up somewhat from 128 if you have a lot of input data.
5. Tweak --num_layers from 2 to 3 but no higher unless you have experience.
6. Tweak --seq_length up from 50 based on the length of a valid input string
   (e.g. names are <= 12 characters, sentences may be up to 64 characters, etc).
   An lstm cell will "remember" for durations longer than this sequence, but the effect falls off for longer character distances.
7. Finally once you've done all that, only then would I suggest adding some dropout.
   Start with --output_keep_prob 0.8 and maybe end up with both --input_keep_prob 0.8 --output_keep_prob 0.5 only after exhausting all the above values.

## Tensorboard

To visualize training progress, model graphs, and internal state histograms: fire up Tensorboard and point it at your `log_dir`. E.g.:

```bash
$ tensorboard --logdir=./logs/
```

Then open a browser to [http://localhost:6006](http://localhost:6006) or the correct IP/Port specified.

## Screenshots

<to be added>

## Project Structure

```
FakeReviewGenerator/
  |- FakeReviewGenerator/
     |- log/
        |- .gitignore
     |- save/
        |- .gitignore
     |- tests/
        |- __init__.py
        |- test_beam.py
        |- test_eval.py
        |- test_example.py
        |- test_train.py
        |- test_utils.py
     |- __init__.py
     |- TextClean.R
     |- beam.py
     |- demo.sh
     |- eval.py
     |- model.py
     |- sample.py
     |- train.py
     |- translate.py
     |- utils.py
  |- data/
     |- tinyshakespeare/
        |- input.txt
     |- pitchfork/
        |- input.txt
     |- extra_inputs/
        |- Kaggle_reduced_2.txt
        |- Kaggle_reduced_3.txt
  |- test_data/
     |- input.txt
     |- pitchfork_test
        |- input.txt
     |- word-rnn-output.txt
  |- doc/
     |- Design Document.md
     |- FakeReviewGeneratorArchitecture.jpg
     |- FunctionalSpecification.md
     |- techreview/
        |- Fake Review Generator Technology Evaluation.pptx
        |- SystemArchitectureDiagram.vsdx
        |- fake-1726362_1920.jpg
        |- tensorflow_eval        
  |- working/
     |- ...
  |- .coveragerc
  |- .travis.yml
  |- .gitignore
  |- LICENSE
  |- README.md
  |- References.txt
  |- requirements.txt
  |- setup.py
```

## Authors

* **_Amitabh Nag_** 
* **_Toan Luong_**
* **_Gautam Moogimane_**

## Acknowledgments

* The guy whose blog started it all, Andrej Karpathy's [char-rnn model](https://github.com/karpathy/char-rnn).
* Our code is mostly from Sung Kim's [word-rnn model](https://github.com/hunkim/word-rnn-tensorflow)

## Contributing

Please feel free to:
* Leave feedback in the issues
* Open a Pull Request
* Share your success stories and data sets!

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

