from setuptools import setup, find_packages

with open('requirements.txt') as f:
	requirements = f.read().splitlines()


setup(
	name='library_manager',
	version='1.2.0',
	packages=find_packages(),
	install_requires=requirements,
	include_package_data=True,
	entry_points={
		'console_scripts' : [
			'library-app=library_app.main:main',
		],
	},
)
