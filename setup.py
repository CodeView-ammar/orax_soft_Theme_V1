from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in orax_soft_Theme_V1/__init__.py
from orax_soft_Theme_V1 import __version__ as version

setup(
	name="orax_soft_Theme_V1",
	version=version,
	description="orax soft Theme for ERPNext / Frappe",
	author="ammar wadood",
	author_email="ammarwadood0@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
