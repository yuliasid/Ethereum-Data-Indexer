from setuptools import setup, find_packages

setup(
    name='ethereum-data-indexer',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['web3'],
    author='Yulia',
    author_email='sidorovajuly@gmail.com',
    description='A tool for indexing Ethereum blockchain data',
    url='https://github.com/yuliasid/Ethereum-Data-Indexer',
    license='MIT',
)
