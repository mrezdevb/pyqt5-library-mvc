from setuptools import setup, find_packages
from setuptools.command.install import install
import sys
from library_app.setup_env import create_env


class PostInstallCommand(install):
	def run(self):
		install.run(self)
		print("\n📦 Running setup_env to create .env file...")
		create_env()




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
			'setup-env=library_app.setup_env:create_env',
			'library-app=library_app.main:main',
		],
	},
	cmdclass={
		'install' : PostInstallCommand,
	},
)
