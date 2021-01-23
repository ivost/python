import platform
import os
import sys
import pathlib

# print(help(platform))

print("Machine network name:", platform.node())
print("Python version:", platform.python_version())
print("System:", platform.system())

print("Python module lookup path:", sys.path)
print("Command to run Python:", sys.argv)

print("user:", os.environ["USER"])
print("current dir:", os.getcwd())

cd = pathlib.Path("")
print("current dir:", os.getcwd())

# files is generator
files = cd.glob("*.py")

# print("py files", list(files))

# [print(f) for f in files]

import subprocess

result = subprocess.run(["ls"])

print("stdout: \n", result.stdout)
