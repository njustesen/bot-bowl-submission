from setuptools import setup, find_packages

setup(name='simplebot',
      version="0.0.1",
      include_package_data=True,
      install_requires=[
          'numpy',
          'ffai'
      ],
      packages=find_packages()
)
