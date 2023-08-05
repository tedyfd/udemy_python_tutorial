myfile = open('section3/myfile.txt')
print(myfile.read())
myfile.seek(0)
print(myfile.readlines())
myfile.close()

# open file without close
with open('section3/myfile.txt') as newfile:
    content = newfile.read()
print(content)

# read
with open('section3/myfile.txt', mode='r') as myfile:
    content = myfile.read()
print(content) 

with open('section3/myfile.txt', mode='a') as myfile:
    myfile.write('\nFour on four')

# read
with open('section3/myfile.txt', mode='r') as myfile:
    print(myfile.read())