from setuptools import setup, find_packages

setup(
    name="sensor",
    version="0.0.1",
    author="Chandan Kumar",
    author_email="chandankm825312@gmail.com",
    packages=find_packages(),
    install_requires=["pymongo"]
)