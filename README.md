# JoinCSV - coding task for VirtusLab BigData intern position
## About
This repository contains tiny CLI program that can join csv files by common, specified column in 3 different modes (like INNER,
LEFT, RIGHT JOIN in SQL) and writes the result to ```stdout```.

## Instalation and usage
This tool was written and tested on Linux, although is should work on Windows and MacOS as well.

On Linux:
- Clone this repository
- Make sure you have [Python 3.10 or newer](https://www.python.org/downloads/) installed
- add ```bin``` directory to ```PATH``` **OR** create symlink in a directory present in ```PATH``` to ```bin/join```

How to use:
```bash
$ join file1 file2 column_name mode
```
where ```file1``` and ```file2``` are files to be joined, ```column_name``` is the name of common column and ```mode``` is
is a mode out of the tree options: ```left```, ```right``` or ```inner```. ```Mode``` can be ommited, ```inner``` is used by
default because it is the default mode in most of SQL flavors (as when JOIN is used without RIGHT, LEFT or INNER, actually
INNER join is performed).

JoinCSV does not support files with columns with matching names (other than the common column specified by an argument). One of the columns will be overwritten. 

## Tests
While in ```test``` directory, you can run
```bash
$ python3 test.py
```
to run the tests which check the basic functionality: correctnes of the headers, merging some example files 
(one to one, one to many, quoted and unquoted values in different quantities). There are no tests against files bigger than
available memory, but that should solved by using Python generators.

## Reasoning
- The time complexity is O(n*m), where n and m are numbers of lines in files, because for every line in one file, every line in second must be checked for matching value. If not for for the fact that input files might be bigger than available memory, 
program could be optimized by, for instance, sorting both files and iterate over them, or sorting one file and, while iterating over the second, serch for values in the first one using binary search. In this case, such solution would be very troublesome, so I decided against it.