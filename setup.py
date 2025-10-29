from setuptools import setup, find_packages
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "RAG medical chatbot",
    version="0.1",
    author= "nidish",
    packages=find_packages(),
    install_requires = requirements,
)