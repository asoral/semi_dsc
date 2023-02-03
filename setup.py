from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in semi_dsc/__init__.py
from semi_dsc import __version__ as version

setup(
	name="semi_dsc",
	version=version,
	description="Semi Digital Signature",
	author="Vaibhav",
	author_email="support@dexciss.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
