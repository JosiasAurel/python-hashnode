from setuptools import setup

setup(
    author="Josias Aurel",
    author_email="ndjosiasaurel@gmail.com",
    name='hashnode',
    install_requires=['gql',],
    version='0.1dev',
    packages=['src',],
    license='MIT',
    url="https://github.com/JosiasAurel/python-hashnode",
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
)
