To build the Python code:
 - install the Python development package
   on Debian this is called e.g. "python2.7-dev" or "python3.2-dev"
   on Fedora "python-devel" for python 2 or "python3-devel" for python 3

 - install the swig package
   on Debian and Fedora this is called "swig"

 - run:
	make cleware_python
   this will produce: _cleware.so and cleware.py.
   These two files must be installed in your Python system.

 - look at example.py to see how it works (e.g. execute python example.py)
   make sure that the user you run your scripts with has enough rights to access the USB devices!
