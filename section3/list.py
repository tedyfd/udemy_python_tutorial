my_list = [1,2,3]
my_list = ['string', 100,23.2]
print(len(my_list))

mylist = ["one", "two", "three"]
anotherlist = ["four", "five"]
print(mylist + anotherlist)

newlist = ["one", "two", "three", "four", "five"]
newlist[0] = "ONE ALL CAPS"
print(newlist)

newlist.append("six")
print(newlist)

newlist.append("seven")
print(newlist)

newlist.pop()
print(newlist)

poppeditem = newlist.pop()
print(newlist)
print(poppeditem)

newlist.pop(0)
print(newlist)

newlist = ['a', 'x', 'd']
newlist.sort()
mysort = newlist
print(mysort)

numlist = [1, 4, 5, 8]
numlist.reverse()
print(numlist)