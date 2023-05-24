from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in passport/__init__.py
from passport import __version__ as version

setup(
	name="passport",
	version=version,
	description="passport",
	author="passport",
	author_email="passport@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
