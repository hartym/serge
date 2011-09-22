from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='serge',
      version=version,
      description="Serge is a badass ORM.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Romain Dorgueil',
      author_email='romain@dorgueil.net',
      url='',
      license='MIT',
      packages=find_packages('./src'),
      package_dir = {'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
      ],
      entry_points="""
      """,
      )
