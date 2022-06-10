import sys

print(sys.argv)
from dir2 import my_mode

try:
    file, hours, rate, bonus = sys.argv
except ValueError:
    print("invalid args")
    exit()
print(my_mode.calculate(int(hours), int(rate), int(bonus)))
