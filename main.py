# Exception Handling

try:
    file = open("test_file.txt")
    test_dictionary = {"key": "value"}
    print(test_dictionary["key"])
except FileNotFoundError:
    file = open("test_file.txt", "w")
    file.write("Something")
except KeyError as error_msg:
    print(f"The key {error_msg} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File is closed.")