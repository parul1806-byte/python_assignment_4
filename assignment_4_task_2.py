#1.   Takes user input and writes it to a file named output.txt.
try:
    text = input("enter the text write to the file:")
    f = open('output.txt', 'w')
    f.write(text + "\n")
    print("data sucessfully written to output.txt\n")
except exception as e:
    print(" error while writing the file",e)
f.close()

#2.Appends additional data to the same file.
try:
    add = input("enter additional data:")
    f = open('output.txt', 'a')
    f.write(add + "\n")
    print("data sucessfully appended\n")
except exception as e:
     print("error while appending the file",e)
f.close()

#3.   Reads and displays the final content of the file.
print("final content of output.txt")
f = open('output.txt','r')
content = f.readlines()
for line in content:
    print(line.strip())
f.close()
