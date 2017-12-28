import sys
from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='gdaxfun',
      version='0.1',
      description='Exmaples and practice on Python coding for Gdax APIs',
      long_description=readme(),
      keywords='gdax crypto bitcoin gdaxfun',
      url='https://github.com/aleecoin/mikeandyrocks/tree/master/python/gdaxfun',
      author='Andrew Lee',
      author_email='doesnotexist@gmail.com',
      license='BSD-3-Clause',
      packages=find_packages(exclude=['tests', 'tests.*']),
      install_requires=[
          'requests',
          'simplejson',
          'pony',
      ],
      extras_require={
          ':python_version<"3.0"': [
          ],
          ':python_version>="3.0"': [
          ],
      },
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
