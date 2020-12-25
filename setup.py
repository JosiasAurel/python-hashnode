from setuptools import setup

setup(
    author="Josias Aurel",
    author_email="ndjosiasaurel@gmail.com",
    name='hashnode',
    install_requires=['gql',],
    version='0.2dev',
    packages=['hashnode',],
    license='MIT',
    url="https://github.com/JosiasAurel/python-hashnode",
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
)
