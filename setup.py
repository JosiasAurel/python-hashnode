from distutils.core import setup

setup(
    author="Josias Aurel",
    author_email="ndjosiasaurel@gmail.com",
    install_requires = ["gql",],
    name='hashnode',
    version='0.1dev',
    packages=['src',],
    license='MIT',
    url="https://github.com/JosiasAurel/python-hashnode",
    long_description=open('README.md').read(),
)
