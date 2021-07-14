from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in insurance_policy/__init__.py
from insurance_policy import __version__ as version

setup(
	name="insurance_policy",
	version=version,
	description="Insurance policy for sales",
	author="Nick",
	author_email="gandhhi.nikhil3@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
