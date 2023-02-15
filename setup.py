from setuptools import setup, find_packages

classifiers  = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Apple :: MacOS :: MacOS Ventura',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='genit',
    version='0.0.1',
    description='Simple integer and string Generator',
    Long_description=open ("README.txt").read() + "\n\n" + open('CHANGELOG.txt').read(),
    url = "", 
    author='Moamal Hussin',
    author_email='dev.moamal@gmail.com',
    License= 'MIT',
    classifiers=classifiers,
    keywordse='',
    packages=find_packages(), 
    install_requires=['']
)
