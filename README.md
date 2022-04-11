<h1 align="center">JoinCSV</h1>
<h3 align="center">Join <i>.csv</i> files based on specified column</h3>

## About
This repository contains tiny CLI program in pure Python that can join csv files by common, specified column in 3 different modes (left, right, inner join, analogical to SQL ```JOIN```) and writes the result to ```stdout```. Works for files with sizes greater than available memory thanks to use of Python generators.

## Instalation
This tool was developed and tested on Linux, although is should work on MacOS and other Unix-like systems as well. Not shure about Windows and
its carriage returns, but I tried to make it the most OS proof as I could, so it should work with very slight changes.

On Linux:
- Make sure you have [Python 3.10 or newer](https://www.python.org/downloads/) present in ```/usr/bin/env```, for instance:
```bash
$ sudo pacman -S python  # on Arch based systems
$ sudo apt update && sudo apt install python3.10  # on Debian based systems
```
- Clone this repository:
```bash
$ git clone https://github.com/LVala/joincsv.git
```
- Add execute permisions to ```bin/join``` file:
```bash
$ chmod +x bin/join
```
- add ```bin``` directory to ```PATH``` **OR** create symlink in a directory present in ```PATH``` to ```bin/join```
**OR** add an alias:
```bash
$ export PATH="path/to/bin:$PATH"  # or
$ ln -s /path/to/bin/join /path/to/dir/in/PATH/join # or
$ alias join='python3 path/to/bin/join'
```

## How to use:
```bash
$ join file1 file2 column_name mode
```
where 
- ```file1``` and ```file2``` are files to be joined 
- ```column_name``` is the name of common column
- ```mode``` is one out of the tree options: ```left```, ```right``` or ```inner```. ```Mode``` can be omitted, in such case ```inner``` is used, as it's the default mode in most of SQL flavors (as when ```JOIN``` is used without ```RIGHT```, ```LEFT``` or ```INNER```, actually ```INNER JOIN``` is performed).

JoinCSV does not support files with columns with matching names (other than the common column specified by an argument). One of the columns will be overwritten. 

## Tests
While in ```test``` directory, you can do
```bash
$ python3 test.py
```
to run the tests which check the basic functionality: correctness of the headers, merging some example files 
(one to one, one to many, quoted and unquoted values in different quantities).

## Reasoning
- The time complexity is ```O(n*m)```, where ```n``` and ```m``` are numbers of lines in the files, because for every line in one file, every line in the second one must be checked for matching value. If not for for the fact that input files might be bigger than available memory, program could be optimized by, for instance, using hashing values or sorting both files and iterate over them or sorting one file and, while iterating over the second, search for values in the first one using binary search. In this case, such solution would be very troublesome, so I decided against it.
