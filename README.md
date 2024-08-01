# Airbnb Clone [Under Development..]
![Project Banner](./images/banner.png)\
![Static Badge](https://img.shields.io/badge/By%20-%20Ahmed%20Aboalesaad-a)\
This project is a sipmle clone of [airbnb.com](https://airbnb.com)\
It implements only the simple featues as a set of modules.

## 1- The Console
The purpose of the console is to separate the logic from other modules.\
It has 2 modes:

1. Interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

2. Non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```