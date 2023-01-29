#!/bin/bash

cd /home/pilks/cs50/python

for d in *;
do cd $d && for d2 in *;
do cd $d2 && yes yes | submit50 cs50/problems/2022/python/$d2 --log-level info;
cd ..
done
cd ..
done