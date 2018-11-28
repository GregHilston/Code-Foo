import sys

err_msg = "You must provide a single non-negative numerical integer."

if len(sys.argv) != 2:
    print(err_msg)
    sys.exit(-1)

try:
    target = int(sys.argv[1])
except:
    print(err_msg)
    sys.exit(-1)

if target < 0:
    print(err_msg)
    sys.exit(-1)

if target == 0:
    print(0)
    sys.exit(0)

n = 0
first = 0
second = 1

while n < target:
    tmp = first
    first = second
    second += tmp
    n += 1

print(second)
