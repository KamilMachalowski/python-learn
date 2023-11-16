import glob

myfiles = glob.glob("excercise-16/files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())