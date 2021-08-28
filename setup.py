"""Mactub - setup.py"""
import sys
import setuptools

try:
    import mactub
except (ImportError, SyntaxError):
    print("Error: mactub requires Python 3.9 or greater.")
    sys.exit(1)

try:
    import pypandoc
    LONG_DESC = pypandoc.convert("README.md", "rst")
except(IOError, ImportError, RuntimeError):
    LONG_DESC = open('README.md').read()

VERSION = mactub.__version__

setuptools.setup(
    name='Mactub',
    version=VERSION,
    packages=['mactub'],
    url='https://github.com/yaqoah/Mactub',
    license='MIT',
    author='Ahmed Yousif',
    author_email='balotelli-7amood@hotmail.com',
    description='View books in a device, read and print synopsis in back',
    long_description=LONG_DESC,
    entry_points={
        "console_scripts":["mactub=mactub.__mactub__:main"]
    },
    python_requires=">=3.9"
)
