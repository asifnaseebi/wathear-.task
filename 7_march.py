import os

def get_contents_of_one_file(file_content):
    file_values = []
    for row in file_content.split("\n")[1:-1]:
        file_values.append(row.split)(",")
    return file_values

def read_files():
    file_names = os.listdir("weatherfiles")

    file_values = []

