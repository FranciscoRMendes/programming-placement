import sys
for linenum, line in enumerate(sys.stdin):
    if linenum == 0:
        no_cases = int(line.split()[0])

print(no_cases)
