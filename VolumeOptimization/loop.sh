#!/bin/bash

python3 scaled.py
for i in {0..4}
do
    pw.x -input input-$i.in > output-$i.out
done
python energy.py
