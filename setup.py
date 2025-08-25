from setuptools import find_packages, setup
from setuptools.command.install import install


class PostInstallCommand(install):
    def run(self) -> None:
        install.run(self)
        print("\n📦 Running setup_env to create .env file...")
        from scripts.setup_env import create_env

        create_env()


with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="library_manager",
    version="2.9.0",
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "setup-env=scripts.setup_env:create_env",
            "library-run = app.main:main",
            "library-install = scripts.install:main",
            "library-uninstall=scripts.uninstall:drop_database",
            "make-lint=scripts.lint_and_type_check:main",
        ],
    },
    cmdclass={
        "install": PostInstallCommand,
    },
)
