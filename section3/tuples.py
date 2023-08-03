t = (1,2,3)
mylist = [1,2,3]

print(type(t))
print(type(mylist))

t = ('a','a','b')
print(t.count('a'))
print(t.index('a'))
print(t.index('b'))

# list
print(mylist)
mylist[0] = 'new'
print(mylist)


#tuples
t[0] = 'new' #error if replace index using tuples
print(t)