import time

start_time = time.time()
input_file_name = "input.txt"
voltage = 0

for line in open(input_file_name):
    voltage += int(line)

print(voltage)

print("--- exeuction took %s seconds ---" % (time.time() - start_time))