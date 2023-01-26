from setuptools import setup

setup(
    name = 'invad',
    version = '0.0.1',
    package = ['invad'],
    entry_points = {"console_scripts":["invad = invad.__main__:main"]},
    install_requires = ['pygame']
)