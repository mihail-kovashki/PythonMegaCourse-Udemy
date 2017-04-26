import datetime
import glob2

final = ""
files = glob2.glob("*.txt")
for file in files:
    with open(file, "r") as read_file:
        final += read_file.read() + "\n"

filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
print(filename)
with open(filename + ".txt", "w") as new_file:
    new_file.write(final)