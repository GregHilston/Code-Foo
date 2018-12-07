import sys

input_file_name = "input.txt"
voltage = 0
voltages = {0: ""}

while True:
    for line in open(input_file_name):
        voltage += int(line)

        if voltage in voltages:
            print(voltage)
            sys.exit(0)
        else:
            voltages[voltage] = ""