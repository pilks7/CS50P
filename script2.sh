#! /bin/bash -p

shopt -s dotglob globstar nullglob
for f in **/*.py; do
  yes yes | submit50 "cs50/problems/2022/python/tests/${f##*/}"
done