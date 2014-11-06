Empirical-CheckStyle
====================

Link to trello board:
https://trello.com/b/QlvMd8iU/empirical-checkstyle


### Some issues and ideas:

* How will you define "famous". By activity, stars?
* It would be interesting to note who the committer was to detect if changes emerge from particular users.
* You might want to take special care to think about how to handle merges from pull requests (or not handle), which would mean bringing in code from a non-contributor.

### Related Work:

* [Prioritizing Warning Categories by Analyzing Software History](https://github.ncsu.edu/CSC510-Fall2014/Empirical-CheckStyle/blob/master/papers/Warnings.pdf?raw=true)

If done well and at a large enough scale, this can make for a nice research paper.

#####Installation of required packages and bundles.

1. cmake : 
```
$ sudo apt-get install cmake
```

2. lib2git : 
```
$ wget https://github.com/libgit2/libgit2/archive/v0.21.2.tar.gz
$ tar xzf v0.21.2.tar.gz
$ cd libgit2-0.21.2/
$ cmake .
$ make
$ sudo make install
$ sudo ldconfig
$ pip3 install pygit2 --user
```

check whether the pygit2 has been installed by running
```
$ python3 -c 'import pygit2'
```

