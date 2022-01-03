# Exception Handling

try:
    file = open("test_file.txt")
    test_dictionary = {"key": "value"}
    print(test_dictionary["new_key"])
except FileNotFoundError:
    file = open("test_file.txt", "w")
    file.write("Something")
except KeyError as error_msg:
    print(f"The key {error_msg} does not exist")