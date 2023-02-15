import os
import subprocess
from setuptools import setup, find_packages

genit_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

if "-" in genit_version:
    # when not on tag, git describe outputs: "1.3.3-22-gdf81228"
    # pip has gotten strict with version numbers
    # so change it to: "1.3.3+22.git.gdf81228"
    # See: https://peps.python.org/pep-0440/#local-version-segments
    v,i,s = genit_version.split("-")
    genit_version = v + "+" + i + ".git." + s

assert "-" not in genit_version
assert "." in genit_version

classifiers  = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Apple :: MacOS :: MacOS Ventura',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='genit',
    version=genit_version,
    description='Simple integer and string Generator',
    Long_description= open("README.md").read() + "\n\n" + open('CHANGELOG.txt').read(),
    url = "https://github.com/devmoamal/genit", 
    author='Moamal Hussin',
    author_email='dev.moamal@gmail.com',
    License= 'MIT',
    classifiers=classifiers,
    python_requires=">=3.5",
    entry_points={"console_scripts": ["gentit = gentit.main:main"]},
    package_data={"genit": ["VERSION"]},
    keywordse='',
    packages=find_packages(), 
    install_requires=['']
)
