from setuptools import find_packages, setup

def get_requirements(path: str):
    return [l.strip() for l in open(path)]

setup(
    name="csv_bots",
    version="0.1.0",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)