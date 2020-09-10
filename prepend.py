import os
def check_if_string_in_file(file_name, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return True
    return False

def read_files(dir):
    string_to_prepend = '"use strict";\n'
    for file in os.listdir(dir):
        if file.endswith(".js"):
            file_path = os.path.join(dir, file)
            if not (check_if_string_in_file(file_path, string_to_prepend)):
                print("writing..." + file)
                write_files(file_path, string_to_prepend)


def write_files(file_name, string_to_write):
    with open(file_name, 'r') as original: data = original.read()
    with open(file_name, 'w') as modified: modified.write(string_to_write + data)


def main():
    dir = ''
    read_files(dir)

if __name__== "__main__":
  main()