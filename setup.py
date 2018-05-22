from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()


--Assumes tensorflow or tensorflow-gpu installed
pip install tensorforce -e .

--Installs with tensorflow-gpu requirement
pip install tensorforce[tf_gpu] -e .

--Installs with tensorflow (cpu) requirement
pip install tensorforce[tf] -e .

-- Install all dependencies from requirements file
pip install -r requirements.txt

extra_packages = {
'tensorflow': ['tensorflow>=1.0.1'],
'tensorflow with gpu': ['tensorflow-gpu>=1.0.1']
}   

install_requires = [
'numpy',
'googletrans'
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
   packages=['scripts'],  
   install_requires=install_requires, #external packages as dependencies
   extras_require=extra_packages
)