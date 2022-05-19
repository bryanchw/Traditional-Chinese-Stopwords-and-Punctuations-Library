from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='TCSP',
  version='0.0.9',
  description='Traditional Chinese Stopwords and Punctuations Library',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',
  author='Bryan Wu',
  author_email='bryanchw@umich.edu',
  license='MIT',
  classifiers=classifiers,
  keywords='stopwords',
  packages=find_packages(),
  install_requires=['']
)
