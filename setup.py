from setuptools import setup, find_packages
from pathlib import Path

ROOT = Path(__file__).resolve().parent

with open(ROOT / 'requirements.txt', 'r') as req_file:
    req_data = req_file.readlines()

setup(
    name='retailta',
    version='0.0.1',
    description='The ta temp project',
    packages=find_packages(include=['retailta', 'retailta.*']),
    install_requires=req_data
)
