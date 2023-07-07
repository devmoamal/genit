from setuptools import setup, find_packages

classifiers  = [
    "Development Status :: 5 - Production/Stable",
    'Intended Audience :: Education',
    'Operating System :: MacOS',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='genit',
    version='0.35',
    description='Simple integer and string Generator',
    Long_description= open("README.md").read() + "\n\n" + open('CHANGELOG.txt').read(),
    url = "https://github.com/devmoamal/genit", 
    author='Moamal Hussin',
    author_email='dev.moamal@gmail.com',
    License= 'MIT',
    classifiers=classifiers,
    python_requires=">=3.5",
    keywordse='',
    packages=find_packages(), 
    install_requires=['']
)
