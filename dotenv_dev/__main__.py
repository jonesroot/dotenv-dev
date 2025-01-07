import os
import re
from typing import Dict, Optional


class DotEnv:
    def __init__(self, file: Optional[str] = None):
        self.dotenv = file if file else ".env"

    def load(self, file: Optional[str] = None):
        if file:
            self.dotenv = file

        if not os.path.exists(self.dotenv):
            raise FileNotFoundError(f"File {self.dotenv} not found!")

        with open(self.dotenv, "r") as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                line = re.sub(r"\s#.*", "", line)

                try:
                    key, val = line.split("=", 1)
                    key = key.strip()
                    val = re.sub('^"|"$', "", val).strip()

                    if not key:
                        raise ValueError("Environment variable key cannot be empty.")
                    os.environ[key] = val
                except ValueError:
                    continue

    def get(self, key: str, default: Optional[str] = None) -> Optional[str]:
        return os.environ.get(key, default)

    def set(self, key: str, value: str):
        if not key:
            raise ValueError("Environment variable key cannot be empty.")
        os.environ[key] = str(value)

    def save(self, file: Optional[str] = None):
        target_file = file if file else self.dotenv
        with open(target_file, "w") as fh:
            for key, value in os.environ.items():
                fh.write(f"{key}={value}\n")

    def delete(self, key: str):
        if key in os.environ:
            del os.environ[key]

    def list_all(self) -> Dict[str, str]:
        return {key: value for key, value in os.environ.items()}


dotenv = DotEnv()
