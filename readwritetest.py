import os 

print(os.path.abspath('.All pys'))
print(os.path.abspath('.'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))
print(os.path.relpath('C:\\Users', 'C:\\desktop\\TEST'))
path = 'C:\\Users\\usuario\\desktop\\test'
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.getsize(path))
print(os.listdir(path))