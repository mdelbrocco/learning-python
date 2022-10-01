import re
import sys

with open(sys.argv[2], "r") as file3:
  for line in file3:
    if re.search(sys.argv[1], line):
      print(line)