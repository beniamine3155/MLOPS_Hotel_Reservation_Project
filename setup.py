from setuptools import setup, find_packages


with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-Hotel-Reservation-Project",
    version="0.1",
    author="Beniamine",
    packages=find_packages(),
    install_requires = requirements
)