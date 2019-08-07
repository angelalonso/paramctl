from setuptools import setup, find_packages
 
setup(name='paramctl',
      version='0.1',
      url='https://github.com/angelalonso/paramctl',
      license='Gnu GPLv3',
      author='Angel Alonso',
      author_email='alonsofonseca.angel@gmail.com',
      description='Define nested parameters accepted via json file',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)
