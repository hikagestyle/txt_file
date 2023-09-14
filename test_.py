import os

dir_name = "dir"

os.makedirs(dir_name, exist_ok=True)

with open('list.txt', 'r') as f:
    List = f.read().split("\n")

for i in List:
    file_path = dir_name + '/' + i + '.txt'
    with open(file_path, 'w') as f:
        f.write('')

# python3 test_.py
