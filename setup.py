import os
import subprocess
from setuptools import setup, find_packages

genit_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

if "-" in genit_version:
    v,i,s = genit_version.split("-")
    genit_version = v + "+" + i + ".git." + s

assert "-" not in genit_version
assert "." in genit_version

assert os.path.isfile("genit/version.py")
with open("genit/VERSION", "w", encoding="utf-8") as fh:
    fh.write("%s\n" % genit_version)

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
