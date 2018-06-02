#!/bin/sh
#This file combines both the training and sampling modules, to sample the output after every one epoch of training.
#It takes 2 parameters, 1 - num of epoch and 2 - seed word to sample with.

j=0

for (( i=0; i < $1; i++ ))
do
	if [ $i -eq 0 ]
	then
		python train.py --num_epochs=1 --rnn_size=512
		python sample.py --prime=$2
	else
		j=$((i + 1))
		python train.py --rnn_size=512 --init_from=save --num_epochs=$j
		python sample.py --prime=$2
	fi
done
exit 0
