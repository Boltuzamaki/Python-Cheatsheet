from setuptools import setup, find_packages

classifiers = [
'Development Status :: 5 - Production/Stable',
'Intended Audience :: Education',
'Operating System :: Microsoft :: Windows 10',
'License :: OSI Approved :: MIT License'
'Programming Language :: Python :: 3'
]

setup(
   name='calculator',
   version='0.0.4',
   description='This is a simple calculator which helps to do airthmetics',
   long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
   url= '',
   author='boltuzamaki',
   author_email='divyanshuboltuzamaki23@gmail.com',
   licence='MIT',
   classifiers=classifiers,
   keywords='calculator',
   packages=['calculator'],
   install_requires=['']
)
