from setuptools import setup, find_packages
setup(
    name = "rdflib-sparql",
    version = "0.1",
    packages = find_packages(),
    install_requires = [ 'pyparsing', 'rdflib>3.2' ],
)
