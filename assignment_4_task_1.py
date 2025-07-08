# Opens and reads a text file named sample.txt
#Prints its content line by line.
try:
    f = open('sample.txt','r')
    content = f.readlines()
    for line in content:
        print(line.strip())

except FileNotFoundError:
    print(" error :The file sample.txt not found")







