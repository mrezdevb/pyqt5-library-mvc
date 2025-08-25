import subprocess
from pathlib import Path
from typing import List


def find_project_root() -> Path:
    current = Path(__file__).resolve()
    while current != current.parent:
        if (current / "setup.py").exists() or (current / "pyproject.toml").exists():
            return current
        current = current.parent
    raise FileNotFoundError(
        "Could not find project root (setup.py or pyproject.toml missing)"
    )


BASE_DIR = find_project_root()
LINT_DIR = BASE_DIR / "lint"


def run(cmd: List[str]) -> int:
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    return result.returncode


def main() -> None:
    run(["black", str(BASE_DIR), "--config", str(LINT_DIR / "pyproject.toml")])
    run(["flake8", str(BASE_DIR), "--config", str(LINT_DIR / ".flake8")])
    run(
        [
            "mypy",
            str(BASE_DIR / "app"),
            str(BASE_DIR / "scripts"),
            "--config-file",
            str(LINT_DIR / "mypy.ini"),
        ]
    )


if __name__ == "__main__":
    main()
