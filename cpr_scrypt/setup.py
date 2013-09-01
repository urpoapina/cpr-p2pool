from distutils.core import setup, Extension

cpr_scrypt_module = Extension('cpr_scrypt',
                               sources = ['scryptmodule.c',
                                          './scrypt-jane/scrypt-jane.c'],
                               include_dirs=['.', './scrypt-jane', './scrypt-jane/code'])

setup (name = 'cpr_scrypt',
       version = '1.0',
       description = 'Bindings for scrypt proof of work used by cpr',
       ext_modules = [cpr_scrypt_module])
