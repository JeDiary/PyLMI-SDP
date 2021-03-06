from os.path import exists
from setuptools import setup


def read_file(name):
    return open(name).read()


description = ('Symbolic linear matrix inequalities (LMI) and semi-definite'
               'programming (SDP) tools for Python')

if exists('README.rst'):
    long_description = read_file('README.rst')
elif exists('README.md'):
    long_description = read_file('README.md')
else:
    long_description = description

setup(
    name='PyLMI-SDP',
    version='1.0-dev',
    author='Cristovao D. Sousa',
    author_email='crisjss@gmail.com',
    description=description,
    license='BSD',
    keywords='LMI SDP',
    url='http://github.com/cdsousa/PyLMI-SDP',
    packages=['lmi_sdp'],
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
    ],
)
