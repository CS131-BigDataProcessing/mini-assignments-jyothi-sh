from setuptools import setup, find_packages
setup(
name='crime_test', 
version='1.0', 
packages=find_packages(),
install_requires=['pandas>=2.2.3'],
description='A package for checking column cleanliness and calculating mean and median', 
author='Jyothi Shankar',
author_email='jyothi.shankar@sjsu.edu',
)
