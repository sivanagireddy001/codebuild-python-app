from setuptools import setup, find_packages

setup(
    name="sample-python-app",
    version="1.0",
    description="A simple Flask application",
    author="siva",
    author_email="siva@example.com",
    packages=find_packages(),
    install_requires=[
        "Flask==2.0.2",
    ],
)
