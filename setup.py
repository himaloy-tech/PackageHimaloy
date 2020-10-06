from setuptools import setup
from PackageHimaloy import *
setup(
    name="PackageHimaloy",
    version="1.1.1",
    description="This is Desc",
    author="Himaloy",
    packages=['PackageHimaloy'],
    install_requires=[]
)
# powershell commands
# python setup.py sdist bdist_wheel
# cd dist
# pip install .\PackageHimaloy-1.1.1-py3-none-any.whl