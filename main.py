# Exception Handling

try:
    file = open("test_file.txt")
except:
    file = open("test_file.txt", "w")
    file.write("Something")