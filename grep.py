import re

file_one = open("new_file.txt", "w") # open (create) file for writing
file_one.write("Coffee\nPlease")
file_one.close()
pattern = "Coffee"
file_one = open("new_file.txt", "r") # open file for reading
for word in file_one:
  if re.search(pattern, word):
    print(word)