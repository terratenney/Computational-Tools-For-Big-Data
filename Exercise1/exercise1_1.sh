#!/bin/bash
#file.txt is test file
tr ' ' '\n' < file.txt | \
tr 'A-Z' 'a-z' | \
tr -d '[:punct:]' | \
sort | \
uniq -c | \
sort -nr | \
cut -c 9- | \
head -10 	   	   
