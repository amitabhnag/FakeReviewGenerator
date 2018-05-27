#!/bin/sh

for (( i=0; i <= $1; i++ ))
do
	if [ $i -eq 0 ]
	then
		python train.py --num_epochs=1 --rnn_size=512
		python sample.py --prime=$2
	else
		python train.py --num_epochs=1 --rnn_size=512 --init_from=save
		python sample.py --prime=$2
	fi
done
exit 0



