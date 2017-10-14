# Combining two lists
numbers = [1, 2, 3, 4]
letters = ['a', 'b']
glenda = numbers + letters
glenda

# see how many methods a declared variable has
dir(glenda)
glenda.reverse()
print 'See what happens when you use the reverse function =  ', glenda

glenda.append(23)
print 'See what happens when you use the append function = ', glenda

glenda.remove(23)
print 'See what happens when you use the remove function = ', glenda
