from setuptools import setup, find_packages
from setuptools.command.install import install
import sys


class PostInstallCommand(install):
	def run(self):
		install.run(self)
		print("\n📦 Running setup_env to create .env file...")
		from scripts.setup_env import create_env
		create_env()


with open('requirements.txt') as f:
	requirements = f.read().splitlines()


setup(
	name='library_manager',
	version='2.5.0',
	packages=find_packages(),
	install_requires=requirements,
	include_package_data=True,
	entry_points={
		'console_scripts' : [
            'setup-env=scripts.setup_env:create_env',
			'library-run = app.main:main',
			'library-install = scripts.install:main',
			'library-uninstall=scripts.uninstall:drop_database',
		],
	},
	cmdclass={
		'install' : PostInstallCommand,
	},
)
