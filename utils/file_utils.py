def create_file(filename):
    with open(filename, "w") as file:
        pass
    print("File created successfully!")
def write_file(filename,data):
    with open(filename, "w") as file:
        file.write(data)
    print("Data written successfully!")
def read_file(filename):
    try:
        with open(filename, "r") as file:
            print("File content :")
            print(file.read())
    except FileNotFoundError:
        print("File not found!")
def append_file(filename, data):
    with open(filename, "a") as file:
        file.write("\n" + data)
    print("Data appended successfully!")