"""Prefer to use your own exception handling class."""
import os


class FileNotFoundError(Exception):
    """Raise the exception when a file is not found."""
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def read_file(file_name: str):
    """Use Iterators instead of Lists when possible"""
    if not os.path.exists(file_name):
        raise FileNotFoundError("This file could not be found anywhere!")
    with open(file_name) as fread:
        for line in fread:
            yield line

for line in read_file("logfile.txt"):
    print(line)