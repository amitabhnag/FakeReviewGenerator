# Setup file for the repo

from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

install_requires = [
'tensorflow>=1.0.1',
'tensorflow-gpu>=1.0.1'
'tensorboard>=1.8.0',
'six>=1.11.0',
'numpy>=1.14.3',
'googletrans>=2.2.0',
'language-check>=1.1',
'pep8>=1.7.0',
'pandas>=0.20.3',
'future>=0.16.0'
]

setup(
   name='fakereviewgenerator',
   version='0.1',
   description='Implementation of a word recurrent neural network using tensorflow to generate fake reviews',
   license='MIT',
   long_description=long_description,
   author='Amitabh Nag, Toan Luong, Gautam Moogimane',
   author_email='amnag@uw.edu, toanlm@uw.edu, mgautam@uw.edu',
   url="https://github.com/amitabhnag/FakeReviewGenerator",
   packages=['fakereviewgenerator'],  
   install_requires=install_requires
)
