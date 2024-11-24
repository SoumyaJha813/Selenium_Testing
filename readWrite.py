#file = open('test.txt')
#Read all the contents of the file
#Read number of characters in a file
#print(file.read(3))
#Reads one single line at a times
#print(file.readline())
#print(file.readline())

#line = file.readline()
#while line!='':
#    print(line)
#    line =  file.readline()

#for line in file.readlines():
#    print(line)
#file.close()

#read the file and store the lines in list
#reverse the list as write back to file
with open('test.txt', 'r') as reader:
    content = reader.readlines() #[abc,efwe,wef,...,rty]
    #reversed(content) #[rty,..,abc]
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

