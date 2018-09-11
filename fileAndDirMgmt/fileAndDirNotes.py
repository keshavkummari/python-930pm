"""**********************************************************"""
# Python Directory and Files Management :


A directory or folder is a collection of files and sub directories.

Python has the os module, which provides us with many useful methods to
work with directories (and files as well).
"""**********************************************************"""
# PYTHON OS Module :

import os
# Executing a shell command
os.system("/root") 
# Get the users environment 
os.environ   
# Returns the current working directory.
os.getcwd()   
# Return the real group id of the current process.
os.getgid()       
# Return the current process’s user id.
os.getuid()    
# Returns the real process ID of the current process.
os.getpid()     
# Set the current numeric umask and return the previous umask.
os.umask(mask)   
# Return information identifying the current operating system.
os.uname()     
# Change the root directory of the current process to path.
os.chroot(path)   
# Return a list of the entries in the directory given by path.
os.listdir(path) 
# Create a directory named path with numeric mode mode.
os.mkdir(path)    
# Recursive directory creation function.
os.makedirs(path)  
# Remove (delete) the file path.
os.remove(path)    
# Remove directories recursively.
os.removedirs(path) 
# Rename the file or directory src to dst.
os.rename(src, dst)  
# Remove (delete) the directory path.
os.rmdir(path)
"""**********************************************************"""
# Get Current Directory :
"""
We can get the present working directory using the getcwd() method.
This method returns the current working directory in the form of a string.
We can also use the getcwdb() method to get it as bytes object.
"""
import os
os.getcwd()
#'C:\\Program Files\\PyScripter'
os.getcwdb()
#b'C:\\Program Files\\PyScripter'
"""Note:
The extra backslash implies escape sequence.
The print() function will render this properly.

print(os.getcwd())
#C:\Program Files\PyScripter"""

"""**********************************************************"""
# Changing Directory :

We can change the current working directory using the chdir() method.

The new path that we want to change to must be supplied as a string to
this method.

We can use both forward slash (/) or the backward slash (\) to separate
path elements.

It is safer to use escape sequence when using the backward slash.

os.chdir('C:\\Python33')

print(os.getcwd())
# C:\Python33
"""**********************************************************"""
# List Directories and Files :

All files and sub directories inside a directory can be known using
the listdir() method.

This method takes in a path and returns a list of sub directories and files in that path.

If no path is specified, it returns from the current working directory.

>>> print(os.getcwd())
C:\Python33

>>> os.listdir()
['DLLs',
'Doc',
'include',
'Lib',
'libs',
'LICENSE.txt',
'NEWS.txt',
'python.exe',
'pythonw.exe',
'README.txt',
'Scripts',
'tcl',
'Tools']

>>> os.listdir('G:\\')
['$RECYCLE.BIN',
'Movies',
'Music',
'Photos',
'Series',
'System Volume Information']
"""**********************************************************"""
# Making a New Directory :

We can make a new directory using the mkdir() method.

This method takes in the path of the new directory.

If the full path is not specified, the new directory is created
in the current working directory.

os.mkdir('test')

os.listdir()
# ['test']
"""**********************************************************"""
# Renaming a Directory or a File :

The rename() method can rename a directory or a file.

The first argument is the old name and the new name must be supplies
as the second argument.

os.listdir()
['test']

os.rename('test','new_one')

os.listdir()
# ['new_one']

"""**********************************************************"""
# Removing Directory or File :

A file can be removed (deleted) using the remove() method.

Similarly, the rmdir() method removes an empty directory.

os.listdir()
# ['new_one', 'old.txt']

os.remove('old.txt')
os.listdir()
# ['new_one']

os.rmdir('new_one')
os.listdir()
# []

However, note that rmdir() method can only remove empty directories.

In order to remove a non-empty directory we can use the rmtree() method
inside the shutil module.

os.listdir()
#['test']

os.rmdir('test')
Traceback (most recent call last):
...
OSError: [WinError 145] The directory is not empty: 'test'

import shutil

shutil.rmtree('test')
os.listdir()
# []
"""**********************************************************"""
# Python file operations :

1. Open a file
2. Read or write (perform operation)
3. Close the file

# Builtin Functions:
1. open()
2. close()

f = open("test_1.txt")    # open file in current directory
f = open("C:/Users/Jessicah Princess/Desktop/test_1.txt")  # specifying full path

"""**********************************************************"""
# Python File Modes:
------------------
Mode	Description
'r'		Open a file for reading. (default)
'w'		Open a file for writing. Creates a new file if it does not 
		exist or truncates the file if it exists.
'x'		Open a file for exclusive creation.
                If the file already exists, the operation fails.
'a'		Open for appending at the end of the file
                without truncating it. 
		Creates a new file if it does not exist.
't'		Open in text mode. (default)
'b'		Open in binary mode.
'+'		Open a file for updating (reading and writing)
"""**********************************************************"""
f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode
"""**********************************************************"""
# Encoding:
The default encoding is platform dependent. 
In windows, it is 'cp1252' but 'utf-8' in Linux. 
"""**********************************************************"""

Closing a file will free up the resources that were tied with the file and
is done using the close() method.

f = open("test.txt",encoding = 'utf-8')
f.read()
f.readlines()
# perform file operations
f.close()

Note: This method is not entirely safe. 

# try...finally method:

If an exception occurs when we are performing some operation with the file, 
the code exits without closing the file. 
A safer way is to use a try...finally block.

try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()
   
Note: This way, we are guaranteed that the file is properly closed even if
an exception is raised, causing program flow to stop.

# with statement :
The best way to do this is using the "with" statement. 
This ensures that the file is closed when the block inside with is exited. 
We dont need to explicitly call the close() method. It is done internally.


with open("test.txt",encoding = 'utf-8') as f:
   # perform file operations

"""**********************************************************"""
# Script mode:

with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")

# Interactive mode:

>>> f = open("test.txt",'r',encoding = 'utf-8')
>>> f.read(4)    # read the first 4 data
'This'
>>> f.read(4)    # read the next 4 data
' is '
>>> f.read()     # read in the rest till end of file
'my first file\nThis file\ncontains three lines\n'
>>> f.read()  # further reading returns empty sting
''
>>> f.tell()    # get the current file position
56
>>> f.seek(0)   # bring file cursor to initial position
0
>>> print(f.read())  # read the entire file
This is my first file
This file
contains three lines

"""**********************************************************"""
We can read a file line-by-line using a for loop. 
This is both efficient and fast.

>>> for line in f:
...     print(line, end = '')
...
This is my first file
This file
contains three lines

Note: The lines in file itself has a newline character '\n'.
Moreover,the print() function also appends a newline by default.
Hence, we specify the end parameter to avoid two newlines when printing.
"""**********************************************************"""
# readline() method to read individual lines of a file :

# This method reads a file till the newline, including the newline character.

>>> f.readline()
'This is my first file\n'

>>> f.readline()
'This file\n'

>>> f.readline()
'contains three lines\n'

>>> f.readline()
''

Lastly, the readlines() method returns a list of remaining lines of the entire file. 
All these reading method return empty values when end of file (EOF) is reached.

>>> f.readlines()
['This is my first file\n', 'This file\n', 'contains three lines\n']
"""**********************************************************"""
Python File Methods:
********************

There are various methods available with the file object. 
Some of them have been used in above examples. 
Here is the complete list of methods in text mode with a brief description.

Python File Methods:
********************
Method		Description
close()		Close an open file. It has no effect if the file is already closed.
detach()	Separate the underlying binary buffer from the TextIOBase and return it.
fileno()	Return an integer number (file descriptor) of the file.
flush()		Flush the write buffer of the file stream.
isatty()	Return True if the file stream is interactive.
read(n)		Read atmost n characters form the file. Reads till end of file if it is negative or None.
readable()	Returns True if the file stream can be read from.
readline(n=-1)	Read and return one line from the file. Reads in at most n bytes if specified.
readlines(n=-1)	Read and return a list of lines from the file. Reads in at most n bytes/characters if specified.
seek(offset,from=SEEK_SET)	Change the file position to offset bytes, in reference to from (start, current, end).
seekable()	Returns True if the file stream supports random access.
tell()		Returns the current file location.
truncate(size=None)	Resize the file stream to size bytes. If size is not specified, resize to current location.
writable()	Returns True if the file stream can be written to.
write(s)	Write string s to the file and return the number of characters written.
writelines(lines)	Write a list of lines to the file.
"""**********************************************************"""


"""**********************************************************"""


"""**********************************************************"""
# Python Exception Handling - Try, Except and Finally :

How to handle exceptions in your Python program using try, except and finally statements.

This will motivate you to write clean, readable and efficient code in Python.

# Flow:

Try(Exception may occur)--> Raise(Raise the exception)-->Excep(Catch if exception occurs)

Python has many built-in exceptions which forces your program to output an error
when something in it goes wrong.

Python (interpreter) raises exceptions when it encounter errors. 

try...finally
The try statement in Python can have an optional finally clause.

This clause is executed no matter what, and is generally used to release external resources.

For example, we may be connected to a remote data center through the network or working
with a file or working with a Graphical User Interface (GUI).

In all these circumstances, we must clean up the resource once used,
whether it was successful or not. These actions (closing a file, GUI or disconnecting from network)
are performed in the finally clause to guarantee execution.

# Here is an example of file operations to illustrate this.

try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()
This type of construct makes sure the file is closed even if an exception occurs.
"""**********************************************************"""

Python Built-in Exceptions:
"""**********************************************************"""

Exception	Cause of Error
AssertionError	Raised when assert statement fails.
AttributeError	Raised when attribute assignment or reference fails.
EOFError	Raised when the input() functions hits end-of-file condition.
FloatingPointError	Raised when a floating point operation fails.
GeneratorExit	Raise when a generator's close() method is called.
ImportError	Raised when the imported module is not found.
IndexError	Raised when index of a sequence is out of range.
KeyError	Raised when a key is not found in a dictionary.
KeyboardInterrupt	Raised when the user hits interrupt key (Ctrl+c or delete).
MemoryError	Raised when an operation runs out of memory.
NameError	Raised when a variable is not found in local or global scope.
NotImplementedError	Raised by abstract methods.
OSError	Raised when system operation causes system related error.
OverflowError	Raised when result of an arithmetic operation is too large to be represented.
ReferenceError	Raised when a weak reference proxy is used to access a garbage collected referent.
RuntimeError	Raised when an error does not fall under any other category.
StopIteration	Raised by next() function to indicate that there is no further item to be returned by iterator.
SyntaxError	Raised by parser when syntax error is encountered.
IndentationError	Raised when there is incorrect indentation.
TabError	Raised when indentation consists of inconsistent tabs and spaces.
SystemError	Raised when interpreter detects internal error.
SystemExit	Raised by sys.exit() function.
TypeError	Raised when a function or operation is applied to an object of incorrect type.
UnboundLocalError	Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
UnicodeError	Raised when a Unicode-related encoding or decoding error occurs.
UnicodeEncodeError	Raised when a Unicode-related error occurs during encoding.
UnicodeDecodeError	Raised when a Unicode-related error occurs during decoding.
UnicodeTranslateError	Raised when a Unicode-related error occurs during translating.
ValueError	Raised when a function gets argument of correct type but improper value.
ZeroDivisionError	Raised when second operand of division or modulo operation is zero.
"""**********************************************************"""
os.getloadavg              os.setegid
os.getlogin                os.seteuid
os.abort                   os.getpgid                 os.setgid
os.getpgrp                 os.setgroups
os.setpgid                 os.setpgrp
os.UserDict                os.getresgid               os.setregid
os.getresuid               os.setresgid               os.getsid
os.setresuid               os.setreuid
os.closerange              os.initgroups              os.setsid
os.confstr                 os.isatty                  os.setuid
os.confstr_names           os.ctermid
os.defpath                 os.devnull
os.link                    os.dup                     os.dup2
os.errno        os.major
os.error                   os.makedev                 os.stat_float_times
os.execl
os.execle                  os.minor                   os.statvfs
os.execlp                  os.statvfs_result
os.execlpe                 os.mkfifo                  os.strerror
os.execv                   os.mknod                   os.symlink
os.execve
os.execvp                  os.sysconf
os.execvpe                 os.open                    os.sysconf_names
os.extsep                  os.openpty                 os.system
os.fchdir                  os.pardir                  os.tcgetpgrp
os.tcsetpgrp    os.pathconf                os.tempnam
os.fdatasync               os.pathconf_names          os.times
os.fdopen                  os.tmpfile
os.pipe                    os.tmpnam
os.forkpty                 os.popen                   os.ttyname
os.fpathconf               os.popen2                  os.popen3
os.fstatvfs                os.popen4
os.fsync                   os.putenv                  os.unsetenv
os.ftruncate               os.read                    os.urandom
os.readlink                os.utime
os.wait                    os.wait3
os.getenv                  os.wait4
os.waitpid                os.getgroups

