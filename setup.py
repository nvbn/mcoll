from setuptools import setup, find_packages

version = '0.1'

setup(name='mcoll',
      version=version,
      description="Modern API for python collection",
      author='Vladimir Iakovlev',
      author_email='nvbn.rm@gmail.com',
      url='https://github.com/nvbn/mcoll',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[])
