#file handling in python 
# file handling allow u to read from and write to fles 
# this is important when u want store data permenantly or work with large datasts
# mode r = read , w - write, a - append 

file = open('test.txt', 'r')

# read file 
# file = open('test.txt', 'r')
# content = file.read()    print all the text value 
# print(content)
# file.close()

# file = open('test.txt', 'r')
# content = file.readline()  # print single line 
# print(content)
# file.close()


file = open('test.txt', 'r')
content = file.readlines()   # print values in list format 
print(content)
file.close()