#!/bin/bash

touch record.txt
for i in {1..15}
do
	pw.x -input input-$i.in > output-$i.out
	echo $i | python3 conv-test.py
done
