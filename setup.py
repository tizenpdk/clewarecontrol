from distutils.core import setup, Extension
srcs = ['cleware_wrap.cxx', 'USBaccessBasic.cpp', 'USBaccess.cpp']
libs = ['hidapi-hidraw']
cleware_module = Extension('_cleware', sources=srcs, libraries=libs)

setup (name = 'cleware',
       version = '2.3',
       author      = "Folkert van Heusden",
       description = """Cleware library bindings for Python""",
       ext_modules = [cleware_module],
       py_modules = ["cleware"],
       )
