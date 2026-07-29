from execution import python
from execution import shell


result = python.execute("""

for i in range(5):

    print(i)

""")

print(result)

print()

cmd = shell.execute("python --version")

print(cmd)