import re

print("-- Example 1 --")

file1 = open("new_file.txt", "w") # open (create) file for writing
file1.write("Coffee\nPlease")
file1.close()
pattern = "Coffee"
file1 = open("new_file.txt", "r") # open file for reading
for word in file1:
  if re.search(pattern, word):
    print(word)

print("-- Example 2 --")

file2 = open("demo.txt", "w")
file2.write("first line of text\nsecond line of text\nthird line of text")
file2.close()

with open("demo.txt", "r") as file2:
  pattern = "second"
  for line in file2:
    if re.search(pattern, line):
      print(line)