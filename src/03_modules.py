"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        print("Argument passed:", arg)
else:
    print("No CL arguments were passed.", end="\n\n")

# Print out the OS platform you're using:
print("OS platform:", sys.platform, end="\n\n")

# Print out the version of Python you're using:
print("Python version:", sys.version, end="\n\n")

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print("Current process ID:", os.getpid(), end="\n\n")

# Print the current working directory (cwd):
print("Working directory:", os.getcwd(), end="\n\n")

# Print out your machine's login name
print("Machine's login name:", os.getlogin())
