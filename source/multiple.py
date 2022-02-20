import sys, ntpath
from os import system as run

print("\n") # just to show their names only.
for i in sys.argv[1:]:
    print(ntpath.basename(i))
print("\n")


# execute it multiple times to make it be able to handle many files at once.
for i in sys.argv:
    if (i == __file__):
        continue
    run(f"python3 SSG.py {i}")
    print(i,"kész")