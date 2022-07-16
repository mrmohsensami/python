"""
    lambda (arguments): manipulate(arguments)
"""

# add = lambda x, y: x + y
# print(add(2,3))



# x = [1, 2, 6, 7, 2, 4, 1, 3]
# print(list(map(lambda i: i*i, x)))

# y = [1, 2, 6, 7, 2, 4, 1, 3]
# print(list(filter(lambda i: i % 2==0, y)))


z = [(4, 'c'), (1, 'a'), (3, 's'), (6, 'b')]
print(sorted(z, key=lambda i: i[1]))
