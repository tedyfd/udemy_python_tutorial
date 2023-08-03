mydict = {'key1':'value1','key2':'value2'}
print(mydict) 
print(mydict['key1'])

d = {'k1':['a','b','c'],'k2':[1,2,3],'k3':{'insidekey':'key3'}}
print(d['k3'])
print(d['k3']['insidekey'])

mylist = d['k1']
print(mylist)

letter = mylist[2]
print(letter)
print(letter.upper())
print(d['k1'][2].upper())


d = {'k1': 100, 'k2': 200, 'k3': 300}
print(d.keys())
print(d.values())
print(d.items())
