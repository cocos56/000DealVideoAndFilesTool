import os

father = os.path.dirname(os.getcwd())
file = father + '\\' + '目录.txt'
fileOpen = open(file, 'r+')
lines = fileOpen.readlines()
fileOpen.close()

i = 0
new_lines = []
for line in lines:
    print(line, end='')
    new_lines.append(line.replace('.mp4', ''))

print()
print()
print()

file = father + '\\' + '目录2.txt'
fileOpen = open(file, 'w+')

for line in new_lines:
    print(line, end='')
    fileOpen.write(line)

fileOpen.close()
