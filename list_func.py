"""
    List Functions
"""

names = ['ali', 'reza', 'bob']
print(names)

names.append('anna')
print(names)

print(len(names))

names.extend(['brad', 'jane'])
print(names)

names.insert(2, 'mohsen')
print(names)

names.remove('jane')
print(names)

names.pop()
print(names)

print(names.index('mohsen'))

print(names.count('mohsen'))

names.sort()
print(names)

names.reverse()
print(names)

names.clear()
print(names)

del names
print(names)
