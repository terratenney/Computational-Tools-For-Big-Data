#!/bin/bash
tr -cs 'a-zA-Z0-9' '[\n*]' < shakespeare.txt | \
tr 'A-Z' 'a-z' | \
sort | \
uniq > shakespeare1.txt

comm -13 <(cat dict | tr 'A-Z' 'a-z' | sort) shakespeare1.txt | \
uniq 


