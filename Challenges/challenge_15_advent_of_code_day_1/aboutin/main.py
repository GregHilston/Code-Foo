import sys

delta = 0

for arg in sys.argv[1:]:
    try:
        delta += int(arg)
    except:
        print("Input frequency changes must be integers.")
        sys.exit(-1)

print("Frequency result: " + str(delta))
