from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="network_calculator",
    version="0.0.1",
    author="Suu Kirinus Nogueira",
    author_email="sknogueira28@gmail.com",
    description="package to calculate sub-networks",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Suu021/DIO-Data-Science/tree/main/network-calculator-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)