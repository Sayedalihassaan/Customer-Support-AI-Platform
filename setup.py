from setuptools import setup, find_packages


with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="Customer Support AI Platform",
    version="0.1.0",
    author="Sayed Ali",
    packages=find_packages() , 
    install_requires= requirements

)