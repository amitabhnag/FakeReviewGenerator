# Example Usage

1. To train and sample together, use the shell script`demo.sh`. The file takes 2 parameters, no of epochs and seed to sample with.

   For each epoch trained, an output will be printed, so one can see the model getting better as the training progresses.

   ![img](/doc/screenshots/demo_command.JPG)

2. To train with default parameters on the pitchfork dataset, run `python train.py`. 

   To access all the parameters use `python train.py --help`.

   To sample from a checkpointed model, `python sample.py`.

The `_sample.py_` file, also includes a grammer check and google translate module as a post processing step.

One can see the grammer check score, and the output quality improving as the training proceeds. 

Sampling while the learning is still in progress (to check last checkpoint) works only in CPU or using another GPU.
To force CPU mode, use `export CUDA_VISIBLE_DEVICES=""` and `unset CUDA_VISIBLE_DEVICES` afterward
(resp. `set CUDA_VISIBLE_DEVICES=""` and `set CUDA_VISIBLE_DEVICES=` on Windows).

To continue training after interruption or to run on more epochs, `python train.py --init_from=save`
