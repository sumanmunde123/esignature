from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in esignature_app/__init__.py
from esignature_app import __version__ as version

setup(
	name="esignature_app",
	version=version,
	description="Esignature App",
	author="doreen",
	author_email="doreenmwapekatebe8@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
