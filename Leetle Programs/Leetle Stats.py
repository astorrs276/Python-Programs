# Program to give me stats about my Leetle programs

import os

paths = ['Leetle Programs\\2025']
filenames = []
one_liners = []
imports = []
classes = []

def get_filenames():
    for path in paths:
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                filenames.append(file_path)

def analyze():
    for filename in filenames:
        with open(filename) as file:
            text = file.read()
            if len(text.split("def solve")[1].split("\n")) == 2:
                one_liners.append(filename)
            if "import" in text:
                imports.append(filename)
            if "class" in text:
                classes.append(filename)

def save():
    with open('Leetle Programs\\one_liners.txt', 'w') as file:
        file.write("\n".join(one_liners))
    with open('Leetle Programs\\imports.txt', 'w') as file:
        file.write("\n".join(imports))
    with open('Leetle Programs\\classes.txt', 'w') as file:
        file.write("\n".join(classes))

def display():
    print("Total:", len(filenames))
    print("One-liners:", len(one_liners))
    print("Imports:", len(imports))
    print("Classes:", len(classes))

def main():
    get_filenames()
    analyze()
    save()
    display()

if __name__ == "__main__":
    main()